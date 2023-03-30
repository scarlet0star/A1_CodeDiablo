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
        self._lv = kwargs.get("lv",1)


    def __str__(self):
        status = f"캐릭터 클래스: {self._classname}\n"
        status += f"레벨: {self._lv}\n\n"
        status += f"체력: {self._max_hp}/{self._hp}/\n"
        status += f"마나: {self._max_mana}/{self._mana}\n"
        status += f"근력: {self._str}\n"
        status += f"민첩: {self._dex}\n"
        status += f"지능: {self._int}\n"
        status += f"의지: {self._will}\n"
        status += f"행운: {self._luck}\n"
        status += f"경험치: {self._exp}\n"

        return status
    
    #장비를 장착하거나 해제 -> 결국 screen에서 결정하는 거니까(stage)
    def update_status(self,**data):
        for key, value in data.items():
            if hasattr(self, key):
                current = getattr(self, key)
                setattr(self, key, current + value)
                
    def updated_by_arms(self,weapon_idx):
        target_weapon = Equip.used_item_list[weapon_idx]
        #weapon 내에 증가하는 스탯들이 stat이라는 딕셔너리에 저장되어있다는 가정하에
        
        for key, value in target_weapon.items():
            if hasattr(self, key):
                current = getattr(self, key)
                setattr(self, key, current - value)
            