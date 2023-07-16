from enum import Enum


class GameMode(Enum):
    ALL = 0
    FREE_FOR_ALL = 1
    TEAM_DEATHMATCH = 2
    TOURNEY = 3
    CAPTURE_THE_FLAG = 4


class Settings:
    mapname: str
    mode: GameMode
    time_limit: int
    frag_limit: int
    capture_limit: int
    max_ping_allowed: int
    min_ping_allowed: int
    max_total_players: int
    max_active_players: int

    def __init__(
        self,
        mapname: str,
        mode: str,
        time_limit: str,
        frag_limit: str,
        capture_limit: str,
        max_ping_allowed: str,
        min_ping_allowed: str,
        max_total_players: str,
        max_active_players: str,
    ):
        self.mapname = mapname
        self.mode = GameMode(int(mode.replace("=", ""))).name
        self.time_limit = int(time_limit)
        self.frag_limit = int(frag_limit)
        self.capture_limit = int(capture_limit)
        self.max_ping_allowed = int(max_ping_allowed)
        self.min_ping_allowed = int(min_ping_allowed)
        self.max_total_players = int(max_total_players)
        self.max_active_players = int(max_active_players)

    def is_free_for_all(self) -> bool:
        return self.mode in [GameMode.ALL.name, GameMode.FREE_FOR_ALL.name]

    def is_tourney(self) -> bool:
        return self.mode == GameMode.TOURNEY.name
