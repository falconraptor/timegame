from typing import List

from tiles import Tile


class Map:
    tiles: List[Tile]

    def __init__(self):
        self.tiles = []
