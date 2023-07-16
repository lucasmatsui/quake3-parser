from enum import Enum
from typing import Any, List, Optional


class TeamsEnum(Enum):
    TEAM_FREE = 0
    TEAM_RED = 1
    TEAM_BLUE = 2
    TEAM_SPECTATOR = 3


class Player:
    client_id: int
    ping: int
    score: int
    nickname: Optional[str]
    character: Optional[str]
    team: TeamsEnum
    health: int
    history_of_weapons: List[str]

    def __init__(
        self,
        client_id: int,
        ping: int,
        score: int,
        nickname: str,
        character: str,
        team: TeamsEnum,
        health: int,
        history_of_weapons: List[str],
    ):
        self.client_id = client_id
        self.ping = ping
        self.score = score
        self.nickname = nickname
        self.character = character
        self.team = team
        self.health = health
        self.history_of_weapons = history_of_weapons

    @staticmethod
    def connect(
        client_id: int, nickname: str, character: str, health: int, team: TeamsEnum
    ) -> "Player":
        return Player(
            client_id=int(client_id),
            ping=0,
            score=0,
            nickname=nickname,
            character=character,
            team=team,
            health=health,
            history_of_weapons=[],
        )

    def dead_by_world(self) -> None:
        self.score -= 1

    def dead_by_own_team(self) -> None:
        self.score -= 1

    def dead_by_himself(self) -> None:
        self.score -= 1

    def kill(self) -> None:
        self.score += 1

    def __eq__(self, other: Any):
        if isinstance(other, Player):
            return self.get_client_id() == other.get_client_id()
        return False

    def get_client_id(self) -> int:
        return self.client_id

    def get_score(self) -> int:
        return self.score

    def get_team(self) -> TeamsEnum:
        return self.team
