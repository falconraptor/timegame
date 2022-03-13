from typing import List

from research import Research
from tools import Tool
from utils import Stack, Tank
from materials import Material


class Station:
    build_time: float
    materials_needed: List[Material]
    research_needed: List[Research]
    input_storage: List[Stack] = None
    output_storage: List[Stack] = None
    input_tanks: List[Tank] = None
    output_tanks: List[Tank] = None

    @property
    def name(self) -> str:
        return self.__name__


class UpgradeableStationMixin:
    upgrade_multiplier: float
    upgrade_time_multiplier: float
    upgrade_stack_input_slots: int = 0
    upgrade_stack_output_slots: int = 0
    upgrade_stack_input_stack_holds: int = 0
    upgrade_stack_output_stack_holds: int = 0
    upgrade_tank_input_slots: int = 0
    upgrade_tank_output_slots: int = 0
    upgrade_tank_input_stack_holds: int = 0
    upgrade_tank_output_stack_holds: int = 0
    xp: int = 0
    level: int = 1
    xp_multiplier: float = 10

    @property
    def xp_needed(self):
        return (1 + self.level) * self.xp_multiplier


class GeneratingStationMixin:
    generates: List[Material]
    generate_time: float
    generate_multiplier: float
    materials_required: List[Material] = None
    requires_manpower: bool = True
    tools_required: List[Tool] = None


class EnergyGeneratingStationMixin(GeneratingStationMixin):
    energy_per_generate: float
    requires_manpower: bool = False
    requires_power: bool = True

    @property
    def energy_per_tick(self) -> float:
        return self.energy_per_generate / (self.generate_time * (self.generate_multiplier + 1) * getattr(self, 'level', 1)) / 10
