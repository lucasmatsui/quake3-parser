import uvicorn
from fastapi import FastAPI
from loguru import logger

from app import env
from app.shared.config.start_load_routes import StartLoadRoutes


class AppBuilder:
    __fastapi: FastAPI

    @staticmethod
    def __start_debugpy() -> None:
        import debugpy

        debugpy.listen(("0.0.0.0", 5678))  # nosec B104
        logger.info("[*] Debug Started!")

    def __start_fastapi(self) -> None:
        self.__fastapi = FastAPI(
            title="quake3-parser",
            description=env(
                "PROJECT_DESCRIPTION_API", cast=str, default="Default Description"
            ),
            version=env("PROJECT_VERSION_API", cast=str, default="Default Version Api"),
        )

        logger.info("[*] FastApi Started!")

    def __start_load_routes(self) -> None:
        logger.info("[*] Load Routes Started!")
        load_routes = StartLoadRoutes(self.__fastapi)
        load_routes.exec()

    @staticmethod
    def start_uvicorn() -> None:
        uvicorn.run(
            "app.main:app",
            host="0.0.0.0",  # nosec B104
            port=8000,
            workers=1,
            reload=True,
        )

        logger.info("[*] Uvicorn Started!")

    def run(self) -> FastAPI:
        if env("DEBUG", cast=bool, default=False):
            self.__start_debugpy()

        self.__start_fastapi()
        self.__start_load_routes()

        return self.__fastapi
