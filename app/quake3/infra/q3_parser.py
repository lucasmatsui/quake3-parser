from typing import List, Optional
from app.quake3.domain.model.game import Game
from app.quake3.infra.q3_connect_player_parser import Q3ConnectPlayerParser
from app.quake3.infra.q3_create_game_parser import Q3CreateGameParser
from app.quake3.infra.q3_kill_parser import Q3KillParser
from app.quake3.infra.q3_event_checker_parser import Q3EventCheckerParser


class Q3Parser:
    games: List[Game]
    current_game: Optional[str]

    def __init__(self) -> None:
        self.games = []
        self.current_game = None

    def parse(self, line: str) -> None:
        event = Q3EventCheckerParser(line)
        game = Q3CreateGameParser(line)
        player = Q3ConnectPlayerParser(line)
        kill = Q3KillParser(line)

        if event.is_started_game():
            self.current_game = game.parse(event.time())
            return

        if event.is_player_connected():
            return self.current_game.connect_player(player.parse())

        if event.is_killed():
            return self.current_game.kill(**kill.parse())

        if event.is_ended_game() and self.current_game:
            return self.end_game(event.time())

    def end_game(self, end_game_time: str) -> None:
        self.current_game.end_game(end_game_time)
        self.games.append(self.current_game)
        self.current_game = None

    def get_games(self) -> List[Game]:
        return self.games
