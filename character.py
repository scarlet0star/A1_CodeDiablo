from equip import Equip

# 캐릭터 클래스입니다.
# __str__을 통해 캐릭터의 정보를 출력할 수 있습니다.


class Character():

    def __init__(self, **kwargs):
        self._classname = kwargs.get("class_name", "NONE")
        self._lv = kwargs.get("lv", 1)

        self._max_hp = kwargs.get("max_hp", 30)
        self._hp = kwargs.get("hp", 30)

        self._max_mana = kwargs.get("max_mana", 30)
        self._mana = kwargs.get("mana", 30)

        self._str = kwargs.get("str", 5)
        self._dex = kwargs.get("dex", 5)
        self._int = kwargs.get("int", 5)
        self._will = kwargs.get("will", 5)
        self._luck = kwargs.get("luck", 5)

        self._exp = kwargs.get("exp", 0)
        self._max_exp = kwargs.get("max_exp", 0)

    def __str__(self):
        status = f"캐릭터 클래스: {self._classname}\n"
        status += f"레벨: {self._lv}\n\n"
        status += f"체력: {self._hp}{self._max_hp}/\n"
        status += f"마나: {self._mana}/{self._max_mana}\n"
        status += f"근력: {self._str}\n"
        status += f"민첩: {self._dex}\n"
        status += f"지능: {self._int}\n"
        status += f"의지: {self._will}\n"
        status += f"행운: {self._luck}\n"
        status += f"경험치: {self._exp}/{self._max_exp}\n"

        return status
