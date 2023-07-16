import pytest
from uuid import UUID
from app.quake3.domain.model.player import Player, TeamsEnum
from app.quake3.domain.model.settings import Settings
from app.quake3.domain.model.teams import Teams
from app.quake3.domain.model.game import Game
from app.quake3.domain.model.death_means import DeathMeans


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


@pytest.fixture
def game_ctf():
    settings = Settings(
        mapname="q3dm17",
        mode="4",
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


def test_connect_more_than_one_player(game: Game):
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

    player3 = Player.connect(
        client_id=int("3"),
        nickname="Frederico",
        character="sarge/default",
        health=int(100),
        team=TeamsEnum(int("3")),
    )

    game.connect_player(player)
    game.connect_player(player2)
    game.connect_player(player3)

    assert len(game.teams.free) == 2
    assert len(game.teams.specs) == 1
    assert game.teams.free.get(player.get_client_id()) == player
    assert game.teams.free.get(player2.get_client_id()) == player2
    assert game.teams.specs.get(player3.get_client_id()) == player3


def test_connect_when_player_change_team(game: Game):
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

    player = Player.connect(
        client_id=int("1"),
        nickname="Isgalamido",
        character="uriel/zael",
        health=int(100),
        team=TeamsEnum(int("3")),
    )

    game.connect_player(player)

    assert len(game.teams.free) == 0
    assert len(game.teams.specs) == 1
    assert game.teams.free.get(player.get_client_id(), None) is None
    assert game.teams.specs.get(player.get_client_id()) == player


def test_when_player_die_to_world(game: Game):
    killer_id = 1022

    player = Player.connect(
        client_id=int("1"),
        nickname="Isgalamido",
        character="uriel/zael",
        health=int(100),
        team=TeamsEnum(int("0")),
    )

    game.connect_player(player)
    game.kill(
        killer_id=killer_id, who_died_id=player.get_client_id(), mean_of_death_id=22
    )
    game.kill(
        killer_id=killer_id, who_died_id=player.get_client_id(), mean_of_death_id=19
    )

    player_founded = game.teams.free.get(player.get_client_id())
    assert player_founded.get_score() == -2
    assert game.kill_by_means.get(DeathMeans.MOD_TRIGGER_HURT.name) == 1
    assert game.kill_by_means.get(DeathMeans.MOD_FALLING.name) == 1
    assert game.total_kills == 2


def test_when_dead_by_himself(game: Game):
    player = Player.connect(
        client_id=int("1"),
        nickname="Isgalamido",
        character="uriel/zael",
        health=int(100),
        team=TeamsEnum(int("0")),
    )

    game.connect_player(player)
    game.kill(
        killer_id=player.get_client_id(),
        who_died_id=player.get_client_id(),
        mean_of_death_id=13,
    )
    game.kill(
        killer_id=player.get_client_id(),
        who_died_id=player.get_client_id(),
        mean_of_death_id=7,
    )

    player_founded = game.teams.free.get(player.get_client_id())
    assert player_founded.get_score() == -2
    assert game.kill_by_means.get(DeathMeans.MOD_BFG_SPLASH.name) == 1
    assert game.kill_by_means.get(DeathMeans.MOD_ROCKET_SPLASH.name) == 1
    assert game.total_kills == 0


def test_when_player_kill_enemies(game_ctf: Game):
    player = Player.connect(
        client_id=int("1"),
        nickname="Isgalamido",
        character="uriel/zael",
        health=int(100),
        team=TeamsEnum(int("1")),
    )

    player2 = Player.connect(
        client_id=int("2"),
        nickname="Isgalamido",
        character="uriel/zael",
        health=int(100),
        team=TeamsEnum(int("2")),
    )

    game_ctf.connect_player(player)
    game_ctf.connect_player(player2)

    game_ctf.kill(
        killer_id=player.get_client_id(),
        who_died_id=player2.get_client_id(),
        mean_of_death_id=6,
    )
    game_ctf.kill(
        killer_id=player.get_client_id(),
        who_died_id=player2.get_client_id(),
        mean_of_death_id=6,
    )

    player_founded = game_ctf.teams.red.get(player.get_client_id())
    player2_founded = game_ctf.teams.blue.get(player2.get_client_id())
    assert player_founded.get_score() == 2
    assert player2_founded.get_score() == 0
    assert game_ctf.kill_by_means.get(DeathMeans.MOD_ROCKET.name) == 2
    assert game_ctf.total_kills == 2


def test_end_game(game: Game):
    ended_match = "22:00"
    game.end_game(ended_match)
    assert game.ended_match == ended_match
