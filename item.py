# 아이템 무기(Weapon) 방어구(Armor) 물약(Potion) 칭호(Title)를 정의하는 클래스 장비(Item)입니다.
#

class Item:
    def __init__(self, **kwargs):
        
        self._name = kwargs.get("name") # get을 사용해 키워드"name" 불러오고 키워드 없으면 none 불러옴
        self._weight = kwargs.get("weight")

        
    def __str__(self): 
        status = f"장비명: {self._name}\n"
        status = f"무게: {self._weight}\n"

        return status
    
class Arms(Item):
    def __init__(self, **kwargs):
        
        self._dmg = kwargs.get("dmg")
        self._mdmg = kwargs.get("mdmg")
        self._def = kwargs.get("def")
        self._mdef = kwargs.get("mdef")
        
    def __str__(self):
        
        status += f"데미지: {self._dmg}\n"
        status += f"마법데미지: {self._mdmg}\n"
        status += f"방어력: {self._def}\n"
        status += f"마법방어력: {self._mdef}\n"
        
        return status
        
class Potion(Item): # 포션을 먹으면 체력회복이 되는 메서드가 담긴 클래스입니다.
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self._amount = kwargs.get("amount", 10)
        self._stat = kwargs.get("stat","hp") # status
    
    def use(self,Character): # 케릭터가 포션을 사용하는 메서드 (main.py와 연결 )
        Character[self._stat] += self._amount
        
    def __str__(self):
        status = f"{self._stat} 회복량: {self._amount}\n"
        return status
        
class Title(Item): # 장착하면 스탯이 증가하는 칭호 메서드가 담긴 클래스입니다.
    def __init__(self,**kwargs):
        super().__init__(self,**kwargs)
        
