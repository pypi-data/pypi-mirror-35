from pathlib import Path

from yamlcfg import YAMLConfig


cfg = YAMLConfig(
    paths=[
        Path('~/.config/apeiron.yaml').expanduser().as_posix(),
        Path('/etc/config/apeiron.yaml').as_posix(),
    ],
    permute=False
)

DEFAULTS = dict(
    storage_dir=Path('~/apeiron/storage').expanduser().as_posix(),
    modpack_index="index.json",
    parallelism=12,
)
