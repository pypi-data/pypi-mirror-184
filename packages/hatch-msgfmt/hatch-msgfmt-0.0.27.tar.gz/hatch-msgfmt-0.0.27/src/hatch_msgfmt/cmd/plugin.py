from typing import Any

from hatch_msgfmt.plugin import BuildHookBase
from typing import BinaryIO
from tempfile import mkstemp
from contextlib import contextmanager
from pathlib import Path
from subprocess import run, DEVNULL
from os import close

@contextmanager
def tempfile(*args, **kwargs):
    handle, pathname = mkstemp(*args, **kwargs)
    close(handle)
    path = Path(pathname)
    try:
        yield path
    finally:
        path.unlink()


class MsgfmtCmdBuildHook(BuildHookBase):
    PLUGIN_NAME = 'msgfmtcmd'

    def convert(self, input: Path) -> bytes:
        with tempfile(suffix='.mo') as file:
            run(['msgfmt', '-o', str(file), str(input)], check=True, stdin=DEVNULL)
            with file.open('rb') as output:
                read = output.read()
                print(read)
                return read
