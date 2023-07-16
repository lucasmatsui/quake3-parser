from uuid import UUID, uuid4
from typing import Dict
from app.quake3.domain.model.death_means import DeathMeans
from app.quake3.domain.model.player import Player
from app.quake3.domain.model.settings import Settings
from app.quake3.domain.model.teams import Teams
from app.shared.aggregate_root import AggregateRoot


@AggregateRoot
class Game:
    def __init__(
        self,
        id: UUID,
        total_kills: int,
        started_match: str,
        ended_match: str,
        settings: Settings,
        teams: Teams,
        kill_by_means: Dict[str, DeathMeans],
    ):
        self.id = id
        self.total_kills = total_kills
        self.started_match = started_match
        self.ended_match = ended_match
        self.settings = settings
        self.teams = teams
        self.kill_by_means = kill_by_means

    @staticmethod
    def create(settings: Settings, started_match: str) -> "Game":
        return Game(
            id=uuid4(),
            settings=settings,
            teams=Teams(free={}, red={}, blue={}, specs={}),
            total_kills=0,
            started_match=started_match,
            ended_match=None,
            kill_by_means={},
        )

    def connect_player(self, player: Player) -> None:
        self.teams.move_player_to_team(player)

    def kill(self, killer_id: int, who_died_id: int, mean_of_death_id: int) -> None:
        # In this game, deaths by enemies are not counted.
        world_killer = 1022
        killer = self.teams.find_connect_player(killer_id)
        who_died = self.teams.find_connect_player(who_died_id)
        mean_of_death = DeathMeans(mean_of_death_id)

        self.count_kill_by_means(mean_of_death)

        if killer_id == world_killer:
            who_died.dead_by_world()
            self.increment_total_kills()
            return self.teams.reorder_player_ranking(who_died)

        if killer == who_died:
            killer.dead_by_himself()
            return self.teams.reorder_player_ranking(killer)

        if self.is_died_by_friendly_fire(killer, who_died):
            who_died.dead_by_own_team()
            return self.teams.reorder_player_ranking(killer)

        killer.kill()
        self.increment_total_kills()
        self.teams.reorder_player_ranking(killer)

    def increment_total_kills(self) -> None:
        self.total_kills += 1

    def is_died_by_friendly_fire(self, killer: Player, who_died: Player):
        is_the_same_team = killer.get_team() == who_died.get_team()
        is_correct_mode = (
            not self.settings.is_free_for_all() and not self.settings.is_tourney()
        )

        return is_correct_mode and is_the_same_team

    def count_kill_by_means(self, mean_of_death: DeathMeans) -> None:
        if self.kill_by_means.get(mean_of_death.name, None):
            self.kill_by_means[mean_of_death.name] += 1
            return

        self.kill_by_means[mean_of_death.name] = 1

    def end_game(self, ended_match: str) -> None:
        self.ended_match = ended_match
