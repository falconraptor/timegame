from typing import List

from biomes import Biome
from materials import Material
from player import Player
from stations import Station


class Tile:
    biome: Biome
    station: Station = None
    meterials: List[Material] = None
    player: Player = None
    passive_gen: List[Material] = None
    passive_time: float = 0
    passive_multiplier: float = 0

    @property
    def name(self) -> str:
        return self.__name__
