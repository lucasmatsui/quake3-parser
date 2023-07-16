from typing import Optional, Dict
from app.quake3.domain.model.player import Player, TeamsEnum


class Teams:
    free: Dict[int, Player]
    red: Dict[int, Player]
    blue: Dict[int, Player]
    specs: Dict[int, Player]

    def __init__(
        self,
        free: Dict[int, Player],
        red: Dict[int, Player],
        blue: Dict[int, Player],
        specs: Dict[int, Player],
    ) -> None:
        self.free = free
        self.red = red
        self.blue = blue
        self.specs = specs

    def reorder_player_ranking(self, player: Player) -> None:
        if player.get_team() == TeamsEnum.TEAM_FREE:
            self.free = dict(
                sorted(
                    self.free.items(),
                    key=lambda player: player[1].get_score(),
                    reverse=True,
                )
            )
            return

        if player.get_team() == TeamsEnum.TEAM_RED:
            self.red = dict(
                sorted(
                    self.red.items(),
                    key=lambda player: player[1].get_score(),
                    reverse=True,
                )
            )
            return

        if player.get_team() == TeamsEnum.TEAM_BLUE:
            self.blue = dict(
                sorted(
                    self.blue.items(),
                    key=lambda player: player[1].get_score(),
                    reverse=True,
                )
            )
            return

    def find_connect_player(self, client_id: int) -> Optional[Player]:
        player = self.free.get(client_id)
        if player:
            return player

        player = self.red.get(client_id)
        if player:
            return player

        player = self.blue.get(client_id)
        if player:
            return player

        return None

    def move_player_to_team(self, player: Player) -> None:
        self.__kick_player_from_teams(player)

        if player.get_team() == TeamsEnum.TEAM_FREE:
            self.free[player.get_client_id()] = player
            return

        if player.get_team() == TeamsEnum.TEAM_RED:
            self.red[player.get_client_id()] = player
            return

        if player.get_team() == TeamsEnum.TEAM_BLUE:
            self.blue[player.get_client_id()] = player
            return

        self.specs[player.get_client_id()] = player
        return

    def __kick_player_from_teams(self, player: Player) -> None:
        self.free.pop(player.get_client_id(), None)
        self.red.pop(player.get_client_id(), None)
        self.blue.pop(player.get_client_id(), None)
        self.specs.pop(player.get_client_id(), None)

    def to_dict(self) -> dict:
        return {
            "free": [player.to_dict() for player in self.free.values()],
            "red": [player.to_dict() for player in self.red.values()],
            "blue": [player.to_dict() for player in self.blue.values()],
            "specs": [player.to_dict() for player in self.specs.values()],
        }
