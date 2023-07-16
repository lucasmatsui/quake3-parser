from typing import List
from app.quake3.domain.model.game import Game
from app.quake3.infra.q3_parser import Q3Parser
import os


class ImportLogFile:
    def __init__(self, q3parser: Q3Parser) -> None:
        self.q3parser = q3parser

    def exec(self) -> List[Game]:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "qgames1.log")

        with open(file_path, "r") as file:
            for line in file:
                self.q3parser.parse(line)

        return self.q3parser.game_list()
