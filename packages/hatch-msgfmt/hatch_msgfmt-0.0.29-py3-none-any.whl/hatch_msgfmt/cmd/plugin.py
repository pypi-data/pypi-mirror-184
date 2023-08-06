from typing import Any

from hatch_msgfmt.plugin import BuildHookBase
from typing import BinaryIO
from tempfile import mkstemp
from contextlib import contextmanager
from pathlib import Path
from subprocess import run, DEVNULL


class MsgfmtCmdBuildHook(BuildHookBase):
    PLUGIN_NAME = 'msgfmtcmd'

    def convert(self, input: Path) -> bytes:
        with tempfile(suffix='.mo') as file:
            run(['msgfmt', '-o', str(file), str(input)], check=True, stdin=DEVNULL)
            with file.open('rb') as output:
                return output.read()
