# 카드를 장비하는 class equip입니다.
# 카드를 추가하는 함수, 장비된 카드의 갯수를 체크하는 함수, 장착된 카드들을 출력하는 함수들이 있습니다.

class Equip:
    def __init__(self):
        self.max = 8

        self._total_skill_list = []
        self._used_skill_list = []

        self._total_item_list = []
        self._used_item_list = []

    def skill_check(self):
        return True if len(self._used_skill_list) < self.max + 1 else False

    def add_skill(self, skill_instance):
        if self.skill_check():
            self._total_skill_list.append(skill_instance)
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
