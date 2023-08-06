from hatchling.plugin import hookimpl
from .plugin import MsgfmtPyBuildHook

@hookimpl
def hatch_register_build_hook():
    return MsgfmtPyBuildHook
