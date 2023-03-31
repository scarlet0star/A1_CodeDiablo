# 획득한 캐릭터와 아이템, 스킬을 보관하고 장착하는 것을 위한 클래스 Equip입니다.
# 

class Equip:
    def __init__(self):
        self.max = 4
        
        self._total_character_list = []

        self._total_skill_list = []
        self._used_skill_list = []
<<<<<<< Updated upstream
=======
        self._used_item_list = {"무기": None,
                                "방어구": None,
                                "칭호": None, }
>>>>>>> Stashed changes

        self._total_item_list = []
        self._used_item_list = []

    def skill_check(self):
        return True if len(self._used_skill_list) < self.max + 1 else False

    def add_skill(self, skill_instance):
<<<<<<< Updated upstream
        if self.skill_check():
            self._total_skill_list.append(skill_instance)
=======
        if isinstance(skill_instance, Skill):
            self._used_skill_list.append(skill_instance)

    def add_item(self, item_instance):
        if isinstance(item_instance, Potion):
            self._potion_list.append(item_instance)
        elif isinstance(item_instance, Arms):
            self._arms_list.append(item_instance)

    def add_character(self, character_instance):
        self._total_character_list.append(character_instance)

    def equip_skill(self, skill_index):
        target = self._total_skill_list[skill_index]
        self._used_skill_list.append(target)
        self._total_skill_list.remove(target)

    def equip_item(self, item_index):
        target = self._arms_list[item_index]
        self._used_item_list.append(target)
        self._arms_list.remove(target)

    def print_total_character_list(self):
        for character in self._total_character_list:
            print(character)

    def print_total_skill_list(self):
        for skill in self._total_skill_list:
            print(skill)

    def print_potion_list(self):
        for potion in self._potion_list:
            print(potion)

    def print_arms_list(self):
        for arms in self._arms_list:
            print(arms)

    def print_used_skill_list(self):
        for skill in self._used_skill_list:
            print(skill)

    def print_used_item_list(self):
        for item in self._used_item_list:
            print(item)

    def print_list(self, idx):
        if idx in self.print_mappings:
            self.print_mappings[idx]()
>>>>>>> Stashed changes
        else:
            while True:
                try:
                    select = int(
                        input("현재 스킬이 모두 장착되어 있습니다. 스킬을 바꾸시겠습니까?\n [1 | 교환하기] [2 | 그만두기]\n >>"))
                    if select == 1:
                        self.card_print()
                        selected = input("\n 교환할 스킬의 번호를 골라주세요. >> ")
                        if 0 < selected <= self.max:
                            self.card_list[selected-1] = skill_instance
                        else:
                            Exception
                except:
                    print("잘못된 입력값입니다.\n")
                    continue

    def __str__(self):
        card_list_str = "{:^5} {:^10} {:^10} {:^15} {:^30}\n".format(
            "장착번호", "카드명", "소모값", "카드 위력", "카드효과")
        for idx, card in enumerate(self.card_list):
            card_str = str(card).split(" / ")
            card_list_str += "{:^10} {:^10} {:^15} {:^15} {:^30}\n".format(
                idx+1, card_str[0], card_str[1], card_str[2], card_str[3]
            )

        return card_list_str
