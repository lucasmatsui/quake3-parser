import re
from app.quake3.domain.model.game import Game
from app.quake3.domain.model.settings import Settings


class Q3CreateGameParser:
    def __init__(self, line: str) -> None:
        self.line = line

    def parse(self, started_game: str) -> "Game":
        settings_pattern = r"(?<=\\)(\w+)\\(.*?)(?=\\|$)"
        configs = dict(re.findall(settings_pattern, self.line))

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
            started_match=started_game,
        )
