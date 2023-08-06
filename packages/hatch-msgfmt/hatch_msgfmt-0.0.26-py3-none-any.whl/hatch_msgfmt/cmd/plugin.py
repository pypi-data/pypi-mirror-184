from typing import Any

from hatch_msgfmt.plugin import BuildHookBase
from typing import BinaryIO
from tempfile import NamedTemporaryFile
from pathlib import Path
from subprocess import run, DEVNULL

class MsgfmtCmdBuildHook(BuildHookBase):
    PLUGIN_NAME = 'msgfmtcmd'

    def convert(self, input: Path) -> bytes:
        with NamedTemporaryFile('rb', suffix='.mo') as file:
            run(['msgfmt', '-o', file.name, str(input)], check=True, stdin=DEVNULL)
            return file.read()
