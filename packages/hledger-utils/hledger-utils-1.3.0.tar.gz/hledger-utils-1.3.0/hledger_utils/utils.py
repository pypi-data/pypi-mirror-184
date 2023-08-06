# SPDX-FileCopyrightText: 2023 Yann Büchau <nobodyinperson@posteo.de>
# SPDX-License-Identifier: GPL-3.0-or-later

# system modules
import logging
import os
import re
import shlex
import shutil
import subprocess
import tempfile
import itertools

# external modules
import psutil

# internal modules


logger = logging.getLogger(__name__)


def find_hledger_command():
    parent = psutil.Process().parent()
    if "hledger" in os.path.basename(cmd := parent.name()):
        return cmd
    else:
        return "hledger"


def sanitize_filename(name):
    return re.sub(r"[^a-z0-9_.+-]+", r"_", str(name), flags=re.IGNORECASE)


def nonempty(x):
    return filter(bool, x)


def vipe(inputstr: str, prefix: str = "", suffix: str = "") -> str:
    if not (
        editor := next(
            (
                editor
                for editor in (
                    [
                        os.environ.get(envvar, "")
                        for envvar in ("VISUAL", "EDITOR")
                    ]
                    + ["nano", "pico", "emacs", "vim", "vi"]
                )
                if shutil.which(next(iter(shlex.split(editor)), ""))
            ),
            None,
        )
    ):
        raise FileNotFoundError(
            "🤷 No Editor found. Set VISUAL or EDITOR environment variable."
        )
    try:
        _, tmpfile = tempfile.mkstemp(prefix=prefix, suffix=suffix)
        logger.debug(f"Filling tempfile {tmpfile!r}")
        with open(tmpfile, "w") as fh:
            fh.write(inputstr)
        editor_cmdparts = shlex.split(editor) + [tmpfile]
        logger.info(f"Launching editor: {editor_cmdparts}")
        subprocess.run(editor_cmdparts)
        logger.debug(f"Reading from tempfile {tmpfile!r}")
        with open(tmpfile, "r") as fh:
            outputstr = fh.read()
    finally:
        try:
            logger.debug(f"🗑️  Removing {tmpfile!r}")
            os.remove(tmpfile)
        except (NameError, OSError) as error:
            logger.error(f"⚠️  Couldn't remove {tmpfile = !r}: {error = !r}")
    return re.sub(r"\n$", r"", re.sub(r"\r\n$", r"", outputstr))


def two_at_a_time(iterable):
    """
    Yields two elements of an iterable at a time. Non-full two-pairs are
    ignored, e.g. when ``iterable`` as an odd numbero of elements.
    """
    iterable = iter(iterable)
    while True:
        try:
            yield next(iterable), next(iterable)
        except StopIteration:
            break


def splitlines(s, linesep=os.linesep):
    """
    Proper version of :any:`str.splitlines` that round-trips with ``linesep.join(s)``.
    """
    return (s + linesep).splitlines()
