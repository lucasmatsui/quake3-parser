from pydantic import BaseModel


class ImportLogFileIn(BaseModel):
    file_path: str
