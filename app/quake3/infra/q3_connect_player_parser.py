import re
from app.quake3.domain.model.player import Player, TeamsEnum


class Q3ConnectPlayerParser:
    def __init__(self, line: str) -> None:
        self.current_line = line

    def parse(self) -> "Player":
        client_id = re.search(r"ClientUserinfoChanged:\s+(\d+)\s", self.current_line)
        nickname = re.search(r"n\\([^\\]+)", self.current_line)
        player_infos = dict(re.findall(r"([^\\]+)\\([^\\]+)", self.current_line))
        player_infos["nickname"] = nickname.group(1)

        return Player.connect(
            client_id=int(client_id.group(1)),
            nickname=player_infos.get("nickname"),
            character=player_infos.get("model"),
            health=int(player_infos.get("hc")),
            team=TeamsEnum(int(player_infos.get("t"))),
        )
