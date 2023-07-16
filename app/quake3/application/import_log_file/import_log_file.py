from typing import List
from app.quake3.application.import_log_file.import_log_file_in import ImportLogFileIn
from app.quake3.domain.model.game import Game
from app.quake3.infra.q3_parser import Q3Parser


class ImportLogFile:
    def __init__(self, q3parser: Q3Parser) -> None:
        self.q3parser = q3parser

    def exec(self, payload: ImportLogFileIn) -> List[Game]:
        with open(payload.file_path, "r") as file:
            for line in file:
                self.q3parser.parse(line)

        return self.q3parser.game_list()
