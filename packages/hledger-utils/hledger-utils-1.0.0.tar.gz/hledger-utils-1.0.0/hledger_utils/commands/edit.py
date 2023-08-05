# SPDX-FileCopyrightText: 2023 Yann Büchau <nobodyinperson@posteo.de>
# SPDX-License-Identifier: GPL-3.0-or-later

# system modules
import argparse
import collections
import difflib
import itertools
import json
import logging
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import textwrap

# external modules
import rich
from rich.console import Console
from rich.logging import RichHandler
from rich.panel import Panel
from rich.pretty import Pretty
from rich.syntax import Syntax

from hledger_utils.utils import find_hledger_command, sanitize_filename, vipe

# internal modules
from hledger_utils.version import __version__

console = Console(stderr=True)
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(
    description="Edit transactions from an hledger query in your $EDITOR"
    f"\n\nversion {__version__}",
    epilog=r"""
❓  Examples
-------------

    # Edit that one transaction with an amount of 103.11 in your $EDITOR
    hledger edit amt:103.11

    # Edit all transactions you made in Europe in 2022 in your $EDITOR
    hledger edit tag:location=Europe date:2022


📝  Specifying Your Editor
---------------------------

Specify your editor via the VISUAL or EDITOR environment variable:

    VISUAL=gedit hledger edit ...

This would launch the 'gedit' editor.


ℹ️  Tip:
--------

You can automate changes by specifying a non-interactive 'editor' like 'sed', 'perl' or 'awk' like this:

    VISUAL='perl -pe "s|Assets:Accounts|assets:accounts|g"' hledger edit ^Assets:Accounts

The above would for example lower-case the account 'Assets:Accounts'.
You can of course do more complex stuff like this.

Written by Yann Büchau, source code is at https://gitlab.com/nobodyinperson/hledger-utils


🐛 Debugging
-------------

    HLEDGER_EDIT_LOGLEVEL=DEBUG hledger edit ...
""",
    formatter_class=argparse.RawDescriptionHelpFormatter,
)
parser.add_argument(
    "--hledger",
    default=find_hledger_command(),
    help="hledger executable to use. "
    "Defaults to the parent process if it looks like hledger.",
)

hledger_parser = argparse.ArgumentParser()
# might later want to catch usage of those options
hledger_parser.add_argument("-O", "--output-format")
hledger_parser.add_argument("-o", "--output-file")


def cli():
    args, hledger_args = parser.parse_known_args()
    logging.basicConfig(
        level=os.environ.get("HLEDGER_EDIT_LOGLEVEL", "INFO"),
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(console=console)],
    )
    logger.debug(f"{args = }")
    logger.debug(f"{hledger_args = }")
    (
        hledger_known_args,
        hledger_remaining_args,
    ) = hledger_parser.parse_known_args(hledger_args)
    logger.debug(f"{hledger_known_args = }")
    logger.debug(f"{hledger_remaining_args = }")
    hledger_cmdparts = [args.hledger, "print"] + hledger_args
    hledger_cmdparts_with_json = hledger_cmdparts + ["-O", "json"]
    try:
        with console.status(
            f"Running {shlex.join(hledger_cmdparts_with_json)!r}"
        ):
            hledger_output = subprocess.check_output(
                hledger_cmdparts_with_json
            )
    except subprocess.CalledProcessError as e:
        logger.error(e)
        sys.exit(1)
    try:
        transactions = json.loads(hledger_output)
    except json.JsonDecodeError as e:
        logger.error(f"💥 Couldn't parse hledger's JSON output. error: {e!r}")
        sys.exit(1)

    logger.info(
        f"hledger found {len(transactions)} transactions "
        f"for query {shlex.join(hledger_args)!r}"
    )

    if not transactions:
        sys.exit(0)

    def file_start_end():
        for i, tx in enumerate(transactions):
            txshort = {
                k: v
                for k, v in tx.items()
                if v and not isinstance(v, (list, dict))
            }
            if not (tsourcepos := tx.get("tsourcepos")):
                logger.info(
                    f"Transaction result nr {i} ({tsummary}) "
                    f"doesn't have a 'tsourcepos', skipping"
                )
                continue
            try:
                sourceNames = set(
                    (pos.get("sourceName", "") or "") for pos in tsourcepos
                )
                if len(sourceNames) != 1:
                    raise TypeError
                sourceLines = set(pos.get("sourceLine") for pos in tsourcepos)
                if not len(sourceLines) == 2 or not all(
                    isinstance(n, int) for n in sourceLines
                ):
                    raise TypeError
            except TypeError:
                logger.info(
                    f"Transaction result nr {i} ({tsummary}) "
                    f"has weird {tsourcepos = }, skipping"
                )
                continue
            location = tuple(list(sourceNames) + sorted(sourceLines))
            logger.debug(f"Transaction nr {i} ({txshort}) {location = }")
            yield location

    locations = list(file_start_end())
    logger.debug(f"{locations = }")

    # aggregate by source file for more efficient lookup
    positionsInSourceFiles = collections.defaultdict(list)
    for sourceFile, lineStart, lineEnd in locations:
        positionsInSourceFiles[sourceFile].append((lineStart, lineEnd))
    logger.debug(f"{positionsInSourceFiles = }")

    # look up transactions in respective files and build a cache
    transactionSources = collections.defaultdict(
        lambda: collections.defaultdict(str)
    )
    sourceFileContents = dict()
    for sourceFile, positions in positionsInSourceFiles.items():
        with open(sourceFile) as fh:
            logger.info(f"Collecting transactions from file {sourceFile!r}")
            content = fh.read()
            sourceFileContents[sourceFile] = content
            lines = content.splitlines()
            for lineStart, lineEnd in positions:
                transactionSources[sourceFile][
                    (lineStart, lineEnd)
                ] = os.linesep.join(lines[slice(lineStart - 1, lineEnd)])

    logger.debug(f"{transactionSources = }")

    # assemble original order from cache
    editorContentParts = [
        f"""
# 🔎  These are the results of the query:
#
#       {shlex.join(hledger_cmdparts)}
#
# 🛑  Only edit the content between the '# [starts|ends] line NNNN in FILE' comments, leave the comments intact.
# If you delete a whole block including the '# starts ...' and '# ends ...' comments, no changes will be applied there.
#
# ✅  If you are done editing, save and close the editor. Your changes will be applied to the respective file locations.
""".strip()
    ]
    for sourceFile, lineStart, lineEnd in locations:
        transactionSource = transactionSources[sourceFile][
            (lineStart, lineEnd)
        ]
        editorContentParts.append(
            f"""
# starts line {lineStart} in {sourceFile}
{transactionSource}
# ends line {lineEnd} in {sourceFile}
""".strip()
        )
    editorContent = (os.linesep * 2).join(editorContentParts)

    editorContentModified = vipe(
        inputstr=editorContent,
        prefix=f"{sanitize_filename(textwrap.shorten(shlex.join(hledger_cmdparts),width=100))}-",
        suffix=".hledger",
    )

    if editorContentModified == editorContent:
        logger.info(f"Nothing changed.")
        sys.exit(0)

    def file_start_end_newcontent():
        lineStartPattern = re.compile(
            r"^#\s+(?P<type>start|end)s\s+line\s+(?P<line>\d+)\s+in\s+(?P<file>.*?)\s*$"
        )
        sourceFile, lineStart, lineEnd, newContentLines = None, None, None, []

        def print_content():
            console.print(
                Panel(
                    os.linesep.join(
                        newContentLines,
                    ),
                    title="Here is the content so far in case you need it",
                    subtitle=f"{sourceFile = }, {lineStart = }, {lineEnd = }",
                    box=rich.box.HORIZONTALS,
                )
            )

        for linenr, line in enumerate(
            editorContentModified.splitlines(), start=1
        ):
            # logger.debug(f"{linenr = }")
            # logger.debug(f"{line = }")
            # logger.debug(f"{lineStart = }")
            # logger.debug(f"{lineEnd = }")
            # logger.debug(f"{newContentLines = }")
            if m := lineStartPattern.fullmatch(line):
                g = m.groupdict()
                if sourceFile is None:
                    sourceFile = g["file"]
                elif sourceFile != g["file"]:
                    logger.error(
                        f"Start/End file don't match in line "
                        "{linenr} ({sourceFile!r} "
                        "vs {g['file']!r}). "
                        "Skipping and starting over."
                    )
                    print_content()
                    sourceFile, lineStart, lineEnd, newContentLines = (
                        None,
                        None,
                        None,
                        [],
                    )
                    continue
                if g["type"] == "start":
                    if lineStart is None:
                        lineStart = int(g["line"])
                    else:
                        logger.error(
                            f"Found another start marker at line {linenr} "
                            f"({line!r}) although the previous one wasn't ended "
                            f"by an end marker. Starting over from here."
                        )
                        print_content()
                        lineEnd, newContentLines = None, []
                    continue
                if g["type"] == "end":
                    if lineStart is None:
                        logger.error(
                            f"Found line end marker at line {linenr} "
                            "but no corresponding start marker. "
                            "Skipping and starting over."
                        )
                        print_content()
                    else:
                        lineEnd = int(g["line"])
                        yield sourceFile, lineStart, lineEnd, os.linesep.join(
                            newContentLines
                        )
                    sourceFile, lineStart, lineEnd, newContentLines = (
                        None,
                        None,
                        None,
                        [],
                    )
                    continue
            elif lineStart is not None:
                newContentLines.append(line)
        if any((sourceFile, lineStart, lineEnd, newContentLines)):
            logger.error(f"Remainder found. Ignoring it.")
            print_content()

    newTransactionSources = collections.defaultdict(
        lambda: collections.defaultdict(str)
    )
    for (
        sourceFile,
        lineStart,
        lineEnd,
        newContent,
    ) in file_start_end_newcontent():
        oldContent = transactionSources[sourceFile][(lineStart, lineEnd)]
        if not oldContent:
            logger.error(
                f"old content for {sourceFile = }, "
                f"{lineStart = }, {lineEnd = } not found"
            )
        if oldContent != newContent:
            logger.debug(f"{oldContent = } != {newContent = }")
            newTransactionSources[sourceFile][
                (lineStart, lineEnd)
            ] = newContent
            if os.environ.get("HLEDGER_EDIT_LOGLEVEL") in {"DEBUG"}:
                console.print(
                    Panel(
                        Syntax(
                            os.linesep.join(
                                list(
                                    difflib.unified_diff(
                                        oldContent.splitlines(),
                                        newContent.splitlines(),
                                        n=1000,
                                    )
                                )[3:]
                            ),
                            lexer="diff",
                        ),
                        title=f"Changes for {sourceFile!r} lines {lineStart}-{lineEnd}",
                    )
                )

    logger.debug(f"{newTransactionSources = }")

    for sourceFile, positions in newTransactionSources.items():
        oldLines = sourceFileContents[sourceFile].splitlines()
        newLines = list(
            itertools.chain.from_iterable(
                oldLines[: lineStart - 1]
                + newContent.splitlines()
                + oldLines[lineEnd - 1 :]
                for (lineStart, lineEnd), newContent in sorted(
                    positions.items()
                )
            )
        )
        console.print(
            Panel(
                Syntax(
                    os.linesep.join(
                        list(
                            difflib.unified_diff(
                                oldLines,
                                newLines,
                                tofile=sourceFile,
                                fromfile=sourceFile,
                                n=10,
                            )
                        )
                    ),
                    lexer="diff",
                ),
                title=f"Changes for {sourceFile!r}",
            )
        )
        prefix, suffix = os.path.splitext(os.path.basename(sourceFile))
        try:
            _, tmpfilePath = tempfile.mkstemp(prefix=prefix, suffix=suffix)
            logger.debug(
                f"Writing content for {sourceFile!r} to {tmpfilePath!r}"
            )
            with open(tmpfilePath, "w") as tmpfile:
                tmpfile.write(os.linesep.join(newLines))
            logger.debug(f"Moving {tmpfilePath!r} to {sourceFile!r}")
            shutil.copy(tmpfilePath, sourceFile)
        finally:
            try:
                os.remove(tmpfilePath)
            except (OSError, FileNotFoundError) as e:
                logger.exception(
                    f"Couldn't delete temporary file {tmpfilePath!r}"
                )


if __name__ == "__main__":
    cli()
