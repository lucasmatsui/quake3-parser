import re
from typing import Dict


class Q3KillParser:
    def __init__(self, line: str) -> None:
        self.current_line = line

    def parse(self) -> Dict[str, int]:
        kill_pattern = re.search(r"(\d+) (\d+) (\d+):", self.current_line)
        killer_id = int(kill_pattern.group(1))
        who_died_id = int(kill_pattern.group(2))
        mean_of_death_id = int(kill_pattern.group(3))

        return {
            "killer_id": killer_id,
            "who_died_id": who_died_id,
            "mean_of_death_id": mean_of_death_id,
        }
