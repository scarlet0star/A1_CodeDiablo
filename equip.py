from skill import Skill
from item import Item, Potion, Weapon
from character import Character


class Equip:
    def __init__(self):
        self.max = 4

        self._total_character_list = []
        self._total_skill_list = []

        self._potion_list = []
        self._arms_list = []

        self._used_skill_list = []
        self._used_item_list = []

    @property
    def used_skill_list(self):
        return self._used_skill_list

    @property
    def used_item_list(self):
        return self._used_item_list

    @property
    def total_character_list(self):
        return self._total_character_list

    @property
    def potion_list(self):
        return self._potion_list

    def skill_check(self):
        return True if len(self._used_skill_list) < self.max + 1 else False

    def add_skill(self, skill_instance):
        if isinstance(skill_instance, Skill):
            self._total_skill_list.append(skill_instance)

    def add_item(self, item_instance):
        if isinstance(item_instance, Potion):
            self._potion_list.append(item_instance)
        elif isinstance(item_instance, Weapon):
            self._arms_list.append(item_instance)

    def add_character(self, character_instance):
        if isinstance(character_instance, Character):
            self._total_character_list.append(character_instance)

    def equip_skill(self, skill_index):
        target = self._total_skill_list[skill_index]
        self._used_skill_list.append(target)
        self._total_skill_list.remove(target)

    def equip_item(self, item_index):
        target = self._arms_list[item_index]
        self._used_item_list.append(target)
        self._arms_list.remove(target)

    def __str__(self, idx):
        if idx == 0:
            card_list_str = "{:^5} {:^10} {:^10} {:^15} {:^30}\n".format(
                "장착번호", "카드명", "소모값", "카드 위력", "카드효과")
            for idx, card in enumerate(self.card_list):
                card_str = str(card).split(" / ")
                card_list_str += "{:^10} {:^10} {:^15} {:^15} {:^30}\n".format(
                    idx+1, card_str[0], card_str[1], card_str[2], card_str[3]
                )
        elif idx == 1:
            pass

        else:
            pass

        return card_list_str
