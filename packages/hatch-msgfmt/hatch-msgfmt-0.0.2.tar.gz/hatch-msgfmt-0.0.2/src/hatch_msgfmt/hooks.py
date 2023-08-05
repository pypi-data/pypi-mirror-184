from typing import Any

from hatchling.builders.hooks.plugin.interface import BuildHookInterface

class MsgfmtBuildHook(BuildHookInterface):
    PLUGIN_NAME = 'msgfmt'

    def initialize(self, version: str, build_data: dict[str, Any]) -> None:
        print('DEBUG HATCH TEST')
        print(version)
        print(repr(build_data))
