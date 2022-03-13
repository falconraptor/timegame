from typing import List

from effects import PlayerEffectMixin, AnimalEffectMixin, EnemyEffectMixin


class Biome:
    movement_modifier: float = 1
    player_effects: List[PlayerEffectMixin] = None
    animal_effects: List[AnimalEffectMixin] = None
    enemy_effects: List[EnemyEffectMixin] = None

    @property
    def name(self) -> str:
        return self.__name__
