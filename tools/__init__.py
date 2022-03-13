from typing import Set

from materials import Material


class Tool(Material):
    durability: int
    max_durability: int
    best_on_material: Set[str] = None  # set of material names
    quantity: int = 1
    maximum_stack: int = 1

    def use(self, material: Material):
        if not self.quantity:
            return False
        per = int(material.name not in self.best_on_material) + 1
        dur = material.quantity * per
        if self.durability > dur:
            self.durability -= dur
            return material
        qty = (dur - self.durability) / per
        self.durability = 0
        self.quantity = 0
        material.quantity -= qty
        return type(material)(qty)
