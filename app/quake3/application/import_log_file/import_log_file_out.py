from pydantic import BaseModel
from typing import List


class GameSettings(BaseModel):
    map: str
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
    kills: int
    deaths: int
    history_of_weapons: List[str]


class GameTeams(BaseModel):
    free: List[Player]
    blue: List[Player]
    red: List[Player]
    specs: List[Player]


class GameModel(BaseModel):
    settings: GameSettings
    teams: GameTeams
    total_kills: int
    match_duration: int
    kills_by_means: List[str]


class ImportLogFileOut(BaseModel):
    games: List[GameModel]
