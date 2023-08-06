from hatchling.plugin import hookimpl
from . import plugins

@hookimpl
def hatch_register_build_hook():
    return [plugins.MsgfmtPyBuildHook, plugins.MsgfmtCmdBuildHook]
