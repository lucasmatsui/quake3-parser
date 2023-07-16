import os
import psutil
import time
from fastapi import APIRouter
from app.quake3.infra.q3_parser import Q3Parser
from app.shared.services.default_presenter import DefaultPresenter

from app.quake3.application.import_log_file.import_log_file import ImportLogFile
from app.quake3.application.import_log_file.import_log_file_in import ImportLogFileIn

router = APIRouter()
router_name = "Quake 3 Parser"


@router.post(
    path="/v1/quake3/logs",
    summary="Import quake3 log",
    operation_id="importQuakeLog",
    status_code=200,
)
async def import_log_file():
    try:
        start_time = time.time()
        start_memory = psutil.virtual_memory().used

        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "../logs/qgames.log")

        usecase = ImportLogFile(Q3Parser())
        output = usecase.exec(ImportLogFileIn(file_path=file_path))

        end_time = time.time()
        end_memory = psutil.virtual_memory().used

        output = {
            "time": f"Duration: {(start_time - end_time)}s",
            "memory": f"Allocate: {(start_memory - end_memory)} bytes",
            "count-games": len(output),
            "games": output,
        }

        return DefaultPresenter.json_success(200, output)
    except FileNotFoundError as fe:
        return DefaultPresenter.json_error(400, str(fe))
