from typing import List

from materials import Material


class Research:
    @property
    def name(self) -> str:
        return self.__name__


class MaterialResearchMixin:
    materials_needed: List[Material]


class TimeResearchMixin:
    time_needed: float


class EnergyResearchMixin(TimeResearchMixin):
    energy_needed: float

    @property
    def energy_per_tick(self) -> float:
        return self.energy_needed / self.time_needed / 10


class RequiresResearchResearchMixin:
    research_requires: List[Research]
