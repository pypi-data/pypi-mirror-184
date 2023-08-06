from .msgfmt import make
from hatch_msgfmt.plugin import BuildHookBase
from pathlib import Path

class MsgfmtPyBuildHook(BuildHookBase):
    PLUGIN_NAME = 'msgfmtpy'

    def convert(self, input: Path) -> bytes:
        with input.open('rb') as file:
            output = make(file)
            print(output)
            return output
