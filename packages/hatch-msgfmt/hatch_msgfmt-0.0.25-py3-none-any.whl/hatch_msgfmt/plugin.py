from typing import Any

from hatchling.builders.hooks.plugin.interface import BuildHookInterface
from typing import BinaryIO
from tempfile import NamedTemporaryFile
from pathlib import Path

class BuildHookBase(BuildHookInterface):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__files = []

    @staticmethod
    def convert(input: Path) -> bytes:
        raise NotImplementedError()

    def initialize(self, version: str, build_data: dict[str, Any]) -> None:
        if self.target_name != 'wheel':
            return

        for file in self.build_config.builder.recurse_included_files():
            path = Path(file.path)
            relative_path = Path(file.relative_path)
            distribution_path = Path(file.distribution_path)
            if distribution_path.suffix == '.po':
                file = NamedTemporaryFile(mode='wb', suffix='.mo')

                file.write(self.convert(path))
                file.flush()

                self.__files.append(file)
                build_data['force_include'][file.name] = str(distribution_path.with_suffix('.mo'))
                print(f'doing {path}')

        if 'exclude' not in build_data:
            build_data['exclude'] = []

        build_data['exclude'].append('*.po')

        print(f'{[(file.path, file.relative_path, file.distribution_path) for file in  self.build_config.builder.recurse_included_files()]=}')

    def finalize(self, version: str, build_data: dict[str, Any], artifact_path: str) -> None:
        if self.target_name != 'wheel':
            return
        print('finalize')
        print(f'{version=}')
        print(f'{build_data=}')
        print(f'{artifact_path=}')
        print(f'{self.directory=}')
        print(f'{self.build_config.directory=}')
        print(f'{self.build_config.default_include()=}')
        print(f'{self.build_config.default_exclude()=}')
        print(f'{self.build_config.default_only_include()=}')
        print(f'{self.build_config.default_packages()=}')
        print(f'{[(file.path, file.relative_path, file.distribution_path) for file in  self.build_config.builder.recurse_included_files()]=}')
