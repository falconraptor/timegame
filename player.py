from typing import List

from utils import Stack


class Player:
    username: str
    xp: int = 0
    level: int = 0
    xp_multiplier: float = 10
    storage: List[Stack] = None

    def __init__(self, name: str):
        self.username = name

    @property
    def xp_needed(self) -> float:
        return (1 + self.level) * self.xp_multiplier
