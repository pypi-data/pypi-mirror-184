from typing import Any

from hatchling.plugin import hookimpl
from hatchling.builders.hooks.plugin.interface import BuildHookInterface
from . import make

class MsgfmtBuildHook(BuildHookInterface):
    PLUGIN_NAME = 'msgfmt'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('INITIALIZING')

    def initialize(self, version: str, build_data: dict[str, Any]) -> None:
        if self.target_name != 'wheel':
            return
        print('initialize')
        print(f'{version=}')
        print(f'{build_data=}')
        print(f'{self.directory=}')

    def finalize(self, *args, **kwargs) -> None:
        if self.target_name != 'wheel':
            return
        print('finalize')

@hookimpl
def hatch_register_build_hook():
    return MsgfmtBuildHook
