class Effect:
    @property
    def name(self) -> str:
        return self.__name__


class PlayerEffectMixin:
    speed_modifier: float = 1


class AnimalEffectMixin:
    speed_modifier: float = 1


class EnemyEffectMixin(AnimalEffectMixin):
    pass
