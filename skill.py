# 카드의 초기화와 출력 그리고 특수 효과에 대한 구현이 있습니다.
# 현재까지 특수효과를 구현하지는 않았지만 card_effect를 통해 특수 효과를 넘겨줍니다.

class Skill:
    def __init__(self, **kwargs):
<<<<<<< Updated upstream
        self.id = kwargs.get("id", 0)
        self.name = kwargs.get("name", "기본 공격")
        self.action = kwargs.get("action", 1)
        self.minV = kwargs.get("minV", 1)
        self.maxV = kwargs.get("maxV", 2)
        self.effect = kwargs.get("effect", None)

    def card_effect(self, *args, **kwargs):
        if self.effect:
            self.effect(*args, **kwargs)
=======
        self._name = kwargs.get("_name", "기본 공격")
        self._mp_cost = kwargs.get("_mp_cost", 0)
        self._hits = kwargs.get("_hits", 1)
        self._damage_per = kwargs.get("_damage_per", 1)
        self._lv = kwargs.get("_lv", 1)
        self._exp = kwargs.get("_exp", 0)
        self._max_exp = kwargs.get("_max_exp", 0)
        self._range = kwargs.get("_range", 0)
>>>>>>> Stashed changes

    def __str__(self):
        status = f"{self.name} / "
        status += f"{self.action} / "
        status += f"{self.minV}~{self.maxV} / "
        status += f"{self.effect}"
        return status
