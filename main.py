from screen import *
from equip import Equip
from skill import Skill
from character import Character
from utils import load_files

# json 파일을 불러옵니다. 이를 통해 json에서 데이터를 꺼내 언제든지 객체를 인스턴스화 할 수 있습니다.
skills = load_files("skill.json")
characters = load_files("character.json")
# items = load_files("item.json")

# 카드 객체를 생성시 사용하는 함수입니다. bool 값으로 player, enemy를 결정합니다.
# Character class 생성시 character.json에 존재하는 기본 스킬 id list를 이용하여 초기 카드 소지 정보를 초기화합니다.

# main 상태입니다. 현재는 스테이지 정보와 player character에 대한 정보밖에 없습니다.


class Player:
    def __init__(self, **data):
        self._propname = data.get("propname", "None")
        self.character = data.get("user", None)
        self._equip = Equip()
        self.stage = 0

        skill = data.get("skill", [])

        # 캐릭터 json 내부에 미리 설정된 skill 목록에 따라 스킬을 획득합니다.
        for skill_name in skill:
            self._equip.add_skill(skill[skill_name])

    def use_item(self, index):
        self._equip.potion_list[index].use(self.character)

    #캐릭터 리스트를 출력해요, 그 캐릭트 리스트에서 유저가 고른 선택지
    def change_class(self, index):
        target_class = self._equip.total_character_list(index)
        self._equip.add_character(self.character)
        self.character = target_class

# main입니다. While 문을 통해 stage.py에서 선택지 정보를 받아와 계속 출력합니다.
# 현재 player 캐릭터를 하나만 지정했기 때문에 **character['1']로 하드코딩 되어있습니다.
# 만약 player 캐릭터를 늘릴 예정이라면 추가적인 선택지를 제시하여 선택할 수 있게 할 예정입니다.


def main():
    user = Character(**characters['1'])
    mainState = Player(**{"propname": "user", "user": user})
    while True:
        text = screen_output(mainState.stage)
        select = get_user_input(text)

        # screen에 있는 stage 딕셔너리 -> 이 안에 현재 스테이지(mainState.stage)로 접근 또 그 안에서 logic에 함수를 불러옴
        next_stage = stage.get(mainState.stage).get("logic")(select, mainState)

        mainState.stage = next_stage


if __name__ == '__main__':
    main()
