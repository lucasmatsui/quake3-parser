from typing import Any
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


class DefaultPresenter:
    @staticmethod
    def json_success(status_code: int, content: Any):
        return JSONResponse(status_code=status_code, content=jsonable_encoder(content))

    @staticmethod
    def json_error(status_code: int, message: str, error_code: int = 2):
        return JSONResponse(
            status_code=status_code,
            content=jsonable_encoder({"code": error_code, "message": message}),
        )
