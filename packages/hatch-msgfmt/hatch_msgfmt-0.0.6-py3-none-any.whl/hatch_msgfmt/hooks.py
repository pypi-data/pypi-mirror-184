from typing import Any

from hatchling.plugin import hookimpl
from hatchling.builders.hooks.plugin.interface import BuildHookInterface

class MsgfmtBuildHook(BuildHookInterface):
    PLUGIN_NAME = 'msgfmt'

    def initialize(self, version: str, build_data: dict[str, Any]) -> None:
        if self.target_name != 'wheel':
            return
        print(f'{version=}')
        print(f'{build_data=}')
        print(f'{self.directory=}')

@hookimpl
def hatch_register_build_hook():
    return MsgfmtBuildHook
