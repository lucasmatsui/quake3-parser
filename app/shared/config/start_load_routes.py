import glob
import importlib
from pathlib import Path
from types import ModuleType
from typing import Optional

from fastapi import FastAPI
from loguru import logger


class StartLoadRoutes:
    __fastapi: FastAPI
    __ignore_files = {"__init__.py", "main.py", "classpath_lo"}

    def __init__(self, fastapi: FastAPI):
        self.__fastapi = fastapi

    def exec(self, child_pathname: Optional[str] = None):
        this_dir = (
            child_pathname if child_pathname else f"{Path(__file__).parent.parent.parent}"
        )
        for path in glob.glob(f"{this_dir}/**/*py", recursive=True):
            if self.__is_module_file(path):
                module_path = self.__convert_to_module_path(path)
                try:
                    module = importlib.import_module(module_path, module_path)
                except Exception as e:
                    logger.exception(f"Failed to load module {module_path}: {e}")
                else:
                    self.__bind_routes(module)

    def __is_module_file(self, file_path: str) -> bool:
        return file_path.endswith(".py") and not any(
            ignore_file in file_path for ignore_file in self.__ignore_files
        )

    @staticmethod
    def __convert_to_module_path(module_file_path: str) -> str:
        refactored_module_path = module_file_path.replace(".py", "").replace("/", ".")
        module_package = refactored_module_path[refactored_module_path.index("app.") :]
        return module_package

    def __bind_routes(self, module: ModuleType):
        router = getattr(module, "router", None)
        if router is not None:
            router_tags = [getattr(module, "router_name", None)] or []
            self.__fastapi.include_router(router, tags=router_tags)  # type: ignore[arg-type]
            logger.info(f"Loaded routes from {module.__name__}")
