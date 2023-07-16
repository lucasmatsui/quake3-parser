import pytest
from uuid import UUID
from app.quake3.domain.model.player import Player, TeamsEnum
from app.quake3.domain.model.settings import Settings
from app.quake3.domain.model.teams import Teams
from app.quake3.domain.model.game import Game


@pytest.fixture
def game():
    settings = Settings(
        mapname="q3dm17",
        mode="0",
        time_limit="15",
        frag_limit="20",
        capture_limit="8",
        max_ping_allowed="0",
        min_ping_allowed="0",
        max_total_players="0",
        max_active_players="16",
    )
    started_match = "00:00"
    return Game.create(settings, started_match)


def test_game_creation():
    game = Game.create(
        settings=Settings(
            mapname="q3dm17",
            mode="0",
            time_limit="15",
            frag_limit="20",
            capture_limit="8",
            max_ping_allowed="0",
            min_ping_allowed="0",
            max_total_players="0",
            max_active_players="16",
        ),
        started_match="00:00",
    )

    assert isinstance(game, Game)
    assert isinstance(game.id, UUID)
    assert game.total_kills == 0
    assert game.started_match == "00:00"
    assert game.ended_match is None
    assert isinstance(game.settings, Settings)
    assert isinstance(game.teams, Teams)
    assert isinstance(game.kill_by_means, dict)


def test_connect_player(game: Game):
    player = Player.connect(
        client_id=int("1"),
        nickname="Isgalamido",
        character="uriel/zael",
        health=int(100),
        team=TeamsEnum(int("0")),
    )

    game.connect_player(player)

    assert len(game.teams.free) == 1
    assert game.teams.free.get(player.get_client_id()) == player
    assert game.teams.free.get(player.get_client_id()).ping == 0
    assert game.teams.free.get(player.get_client_id()).score == 0
    assert game.teams.free.get(player.get_client_id()).nickname == "Isgalamido"
    assert game.teams.free.get(player.get_client_id()).character == "uriel/zael"
    assert game.teams.free.get(player.get_client_id()).health == 100
    assert game.teams.free.get(player.get_client_id()).team == TeamsEnum.TEAM_FREE


def test_connect_two_players(game: Game):
    player = Player.connect(
        client_id=int("1"),
        nickname="Isgalamido",
        character="uriel/zael",
        health=int(100),
        team=TeamsEnum(int("0")),
    )

    player2 = Player.connect(
        client_id=int("2"),
        nickname="Kenzo",
        character="xian/default",
        health=int(100),
        team=TeamsEnum(int("0")),
    )

    game.connect_player(player)
    game.connect_player(player2)

    assert len(game.teams.free) == 2
    assert game.teams.free.get(player.get_client_id()) == player
    assert game.teams.free.get(player2.get_client_id()) == player2
