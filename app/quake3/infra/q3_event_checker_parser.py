import re
from typing import Optional


class Q3EventCheckerParser:
    def __init__(self, line: str) -> None:
        self.command_pattern = r"(\d+:\d+) ([A-Za-z]+):|(\d+:\d+) (-+)"
        self.current_line = line

    def is_started_game(self) -> bool:
        return bool(self.__command() == "InitGame")

    def is_player_connected(self) -> bool:
        return bool(self.__command() == "ClientUserinfoChanged")

    def is_killed(self) -> bool:
        return bool(self.__command() == "Kill")

    def is_ended_game(self) -> bool:
        shutdowngame = bool(self.__command() == "ShutdownGame")
        endgame_without_shutdown = bool(self.__command() == "EndgameWithoutShutdown")

        return shutdowngame or endgame_without_shutdown

    def __command(self) -> Optional[str]:
        command = re.search(self.command_pattern, self.current_line)

        if command is None:
            return None

        return command.group(2) or "EndgameWithoutShutdown"

    def time(self) -> Optional[str]:
        time = re.search(self.command_pattern, self.current_line)

        if time is None:
            return None

        return time.group(1) or time.group(3)
