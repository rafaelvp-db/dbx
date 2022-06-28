import pathlib
from typing import Optional

from dbx.constants import CONTEXT_INFO_PATH
from dbx.models.context import ContextInfo
from dbx.utils.json import JsonUtils


class LocalContextManager:
    context_file_path: pathlib.Path = CONTEXT_INFO_PATH

    @classmethod
    def set_context(cls, context: ContextInfo) -> None:
        JsonUtils.write(cls.context_file_path, context.dict())

    @classmethod
    def get_context(cls) -> Optional[ContextInfo]:
        if cls.context_file_path.exists():
            return ContextInfo(**JsonUtils.read(cls.context_file_path))
        else:
            return None
