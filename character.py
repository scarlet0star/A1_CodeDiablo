from equip import Equip

# 캐릭터 클래스입니다.
# 초기 카드 정보를 초기화할때 json의 초기 카드 id 리스트를 받아와 equip 내의 card 리스트를 구성합니다.
# __str__을 통해 캐릭터의 정보를 출력할 수 있습니다.


class Character():

    def __init__(self, **kwargs):
        self._classname = kwargs.get("classname", "NONE")

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


    def __str__(self):
        status = f"캐릭터 클래스: {self._classname}\n"
        status += f"최대 HP: {self._max_hp}\n"
        status += f"현재 HP: {self._hp}\n"
        status += f"최대 마나: {self._max_mana}\n"
        status += f"현재 마나: {self._mana}\n"
        status += f"힘: {self._str}\n"
        status += f"민첩: {self._dex}\n"
        status += f"지능: {self._int}\n"
        status += f"의지: {self._will}\n"
        status += f"운: {self._luck}\n"
        status += f"경험치: {self._exp}\n"

        return status
