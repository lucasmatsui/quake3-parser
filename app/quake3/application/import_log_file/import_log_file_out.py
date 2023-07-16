from pydantic import BaseModel
from typing import List, Dict


class GameSettings(BaseModel):
    mapname: str
    mode: str
    time_limit: int
    frag_limit: int
    capture_limit: int
    max_ping_allowed: int
    min_ping_allowed: int
    max_total_players: int
    max_active_players: int


class Player(BaseModel):
    client_id: int
    ping: int
    score: int
    nickname: str
    character: str
    health: int
    history_of_weapons: List[str]


class GameTeams(BaseModel):
    free: List[Player]
    blue: List[Player]
    red: List[Player]
    specs: List[Player]


class GameModel(BaseModel):
    total_kills: int
    started_match: str
    ended_match: str
    settings: GameSettings
    teams: GameTeams
    kills_by_means: Dict[str, int]


class ImportLogFileOut(BaseModel):
    games: List[GameModel]
