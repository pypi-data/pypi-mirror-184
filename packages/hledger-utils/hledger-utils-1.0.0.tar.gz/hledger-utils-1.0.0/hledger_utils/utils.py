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
            nonempty(
                shutil.which(shlex.split(editor)[0])
                for editor in (
                    [
                        os.environ.get(envvar, "")
                        for envvar in ("VISUAL", "EDITOR")
                    ]
                    + ["nano", "pico", "emacs", "vim", "vi"]
                )
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
            os.remove(tmpfile)
        except (NameError, OSError) as error:
            logger.error(f"⚠️  Couldn't remove {tmpfile = !r}: {error = !r}")
    return outputstr.removesuffix("\r\n").removesuffix("\n")
