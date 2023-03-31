# 범위 공격은 아직 구현하기 힘드니 나중에 넣을 예정


# battle.py


class Skill:
    def __init__(self, **kwargs):
        self._name = kwargs.get("name", "기본 공격")
        self._mp_cost = kwargs.get("mp_cost", 0)
        self._hits = kwargs.get("hits", 1)
        self._damage_per = kwargs.get("damage_per", 1)
        self._lv = kwargs.get("lv", 1)
        self._exp = kwargs.get("exp", 0)
        self._max_exp = kwargs.get("max_exp", 0)
        self._range = kwargs.get("range", 0)

    def __str__(self):
        status = f"{self._name=}"
        status += f"{self._mp_cost=}"
        status += f"{self._hits=}"
        status += f"{self._damage_per=}"
        status += f"{self._lv=}"
        status += f"{self._exp} / {self._max_exp}"

        # status += f"{self.action} / "
        # status += f"{self.minV}~{self.maxV} / "
        # status += f"{self.effect}"
        return status
