from .msgfmt import make
from hatch_msgfmt.plugin import BuildHookBase
from pathlib import Path

class MsgfmtPyBuildHook(BuildHookBase):
    PLUGIN_NAME = 'msgfmtpy'

    @staticmethod
    def convert(input: Path) -> bytes:
        with input.open('rb') as file:
            return make(file)
