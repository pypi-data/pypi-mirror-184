from .msgfmt import make
from hatch_msgfmt.plugin import BuildHookBase
from pathlib import Path

class MsgfmtPyBuildHook(BuildHookBase):
    PLUGIN_NAME = 'msgfmtpy'

    @staticmethod
    def convert(input: Path) -> bytes:
        print(f'converting {input}')
        with input.open('r') as file:
            print(f'{file.read()=}')
        with input.open('rb') as file:
            return make(file)
