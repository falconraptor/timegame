from typing import Optional

from materials import Material, Fluid


class Stack:
    __holds: int
    material: Optional[Material] = None

    @property
    def holds(self):
        if self.material and self.material.maximum_stack:
            if self.material.maximum_stack > self.__holds:
                return self.__holds
            return self.material.maximum_stack
        return self.__holds


class Tank(Stack):
    __holds: float
    material: Optional[Fluid] = None
