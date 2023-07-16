import re
from typing import List, Match, Optional
from app.quake3.domain.model.game import Game
from app.quake3.domain.model.player import Player, TeamsEnum
from app.quake3.domain.model.settings import Settings


class Q3Parser:
    def __init__(self) -> None:
        self.command_pattern = r"(\d+:\d+) ([A-Za-z]+):|(\d+:\d+) (-+)"
        self.games = []
        self.current_game = None
        self.current_line = None

    def parse(self, line: str) -> None:
        self.current_line = line

        if self.is_start_game():
            self.current_game = self.create_game()
            return

        if self.is_player_connect():
            self.connect_player()
            return

        if self.is_kill():
            self.kill()
            return

        if self.is_end_game():
            self.current_game.end_game(self.get_end_match())
            self.games.append(self.current_game)
            self.current_game = None
            return

    def create_game(self) -> "Game":
        configs = self.get_map_setting()

        return Game.create(
            settings=Settings(
                mapname=configs.get("mapname"),
                mode=configs.get("g_gametype"),
                time_limit=configs.get("timelimit"),
                frag_limit=configs.get("fraglimit"),
                capture_limit=configs.get("capturelimit"),
                max_ping_allowed=configs.get("sv_maxPing"),
                min_ping_allowed=configs.get("sv_minPing"),
                max_total_players=configs.get("g_maxGameClients"),
                max_active_players=configs.get("sv_maxclients"),
            ),
            started_match=self.get_start_match(),
        )

    def connect_player(self) -> None:
        client_id = re.search(r"ClientUserinfoChanged:\s+(\d+)\s", self.current_line)
        nickname = re.search(r"n\\([^\\]+)", self.current_line)
        player_infos = dict(re.findall(r"([^\\]+)\\([^\\]+)", self.current_line))
        player_infos["nickname"] = nickname.group(1)

        player = Player.connect(
            client_id=int(client_id.group(1)),
            nickname=player_infos.get("nickname"),
            character=player_infos.get("model"),
            health=int(player_infos.get("hc")),
            team=TeamsEnum(int(player_infos.get("t"))),
        )

        self.current_game.connect_player(player)

    def kill(self) -> None:
        kill_pattern = re.search(r"(\d+) (\d+) (\d+):", self.current_line)
        killer_id = int(kill_pattern.group(1))
        who_died_id = int(kill_pattern.group(2))
        meand_of_death_id = int(kill_pattern.group(3))

        self.current_game.kill(killer_id, who_died_id, meand_of_death_id)

    def is_start_game(self) -> bool:
        return bool(self.command() == "InitGame")

    def is_player_connect(self) -> bool:
        return bool(self.command() == "ClientUserinfoChanged")

    def is_kill(self) -> bool:
        return bool(self.command() == "Kill")

    def is_end_game(self) -> bool:
        shutdowngame = bool(self.command() == "ShutdownGame")
        endgame_without_shutdown = (
            bool(self.command() == "EndgameWithoutShutdown") and self.current_game
        )

        return shutdowngame or endgame_without_shutdown

    def command(self) -> Optional[str]:
        command = re.search(self.command_pattern, self.current_line)

        if command is None:
            return None

        return command.group(2) or "EndgameWithoutShutdown"

    def time(self) -> Optional[str]:
        time = re.search(self.command_pattern, self.current_line)

        if time is None:
            return None

        return time.group(1) or time.group(3)

    def get_start_match(self) -> Optional[Match[str]]:
        return self.time()

    def get_end_match(self) -> Optional[Match[str]]:
        return self.time()

    def get_map_setting(self) -> dict:
        settings_pattern = r"(?<=\\)(\w+)\\(.*?)(?=\\|$)"
        return dict(re.findall(settings_pattern, self.current_line))

    def game_list(self) -> List[Game]:
        return self.games
