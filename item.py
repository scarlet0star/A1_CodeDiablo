# 아이템 무기(Weapon) 방어구(Armor) 물약(Potion) 칭호(Title)를 정의하는 클래스 장비(Item)입니다.
#

class Item:
    
    def __init__(self, **kwargs):
        
        self._name = kwargs.get("name")
        self._weight = kwargs.get("weight")
        self._dmg = kwargs.get("dmg", 30)
        self._magicdmg = kwargs.get("magicdmg", 30)
        self._def = kwargs.get("def", 30)
        self._magicdef = kwargs.get("mana", 30)
        
    def __str__(self): 
        
        status = f"장비명: {self._name}\n"
        status = f"무게: {self._weight}\n"
        status += f"무게없음: {self._weight}\n"
        status += f"데미지: {self._dmg}\n"
        status += f"마법데미지: {self._magicdmg}\n"
        status += f"방어력: {self._def}\n"
        status += f"마법방어력: {self._magicdef}\n"

        return status
        
class Potion(Item): # 포션을 먹으면 체력회복이 되는 메서드가 담긴 클래스입니다.
    def __init__(self,amount):
        super().__init__(self, **kwargs)
        self._amount = amount.get("amount", 10)
    
    def use(self,Character): # 케릭터가 포션을 사용하는 메서드
        self.use = Character[self._amount] += self._amount
        
    def __str__(self):
        
        status += f"hp회복량: {self._amount}\n"
        status += f"mp회복량: {self._amount}\n"
 
        return status
        
class Title(Item): # 장착하면 스탯이 증가하는 칭호 메서드가 담긴 클래스입니다.
    def __init__(self, sum):
        super().__init__(self, )