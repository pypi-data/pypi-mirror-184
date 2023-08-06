from hatchling.plugin import hookimpl
from .plugin import MsgfmtCmdBuildHook

@hookimpl
def hatch_register_build_hook():
    return MsgfmtCmdBuildHook
