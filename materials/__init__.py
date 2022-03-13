from typing import Optional


class Material:
    quantity: float = 0
    maximum_stack: Optional[int] = None

    @property
    def name(self) -> str:
        return self.__name__


class Fluid(Material):
    quantity: float = 0
    maximum_stack: Optional[float] = None
