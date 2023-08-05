import sys
from pathlib import Path
from typing import Union

from autologging import traced

this = sys.modules[__name__]
this.appBase: Path = Path(__file__).parent.parent
this.logBase: Path = this.appBase.joinpath('logs')


@traced
def join(*paths: Union[tuple, str]) -> Path:
	return Path(*paths)


@traced
def fileDirJoin(_file_: str, *paths: Union[tuple, str]) -> Path:
	return Path(_file_).parent.joinpath(*paths).resolve()


@traced
def app(*paths: Union[tuple, str]) -> Path:
	return this.appBase.joinpath(*paths)


@traced
def log(*paths: Union[tuple, str]) -> Path:
	return this.logBase.joinpath(*paths)
