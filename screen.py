# from battle import Battle
# from character import Character
# from main import enemies
import time
import os
from utils import pick
import scripts

def battle_stage(mainState):
    return mainState.stage


def view_skill(mainState):
    mainState._equip.print_list(1)
    return mainState.stage


def view_inventory(mainState):
    mainState._equip.print_list(2)
    print("포션은 전투 중에 사용가능합니다\n")
    mainState._equip.print_list(3)
    idx = input("장착하고 싶은 ")
    return mainState.stage


def view_status(mainState):
    print(mainState.character)
    return mainState.stage


def view_used_skill(mainState):
    mainState._equip.print_list(4)
    return mainState.stage


def view_equip(mainState):
    mainState._equip.print_list(5)
    return mainState.stage


def change_char(mainState):
    mainState._equip.print_list(0)
    return mainState.stage


def back(mainState):
    os.system('cls')
    return mainState.stage


action_function = {0: battle_stage,
                   1: view_skill,
                   2: view_inventory,
                   3: view_status,
                   4: view_used_skill,
                   5: view_equip,
                   6: change_char,
                   7: back, }

selection = ["이동", "행동"]

places = {
    0: ["[여관]", "여관에서는 다양한 모험가들이 쉬고 있습니다. 따뜻한 분위기와 향긋한 음식 냄새가 흐릅니다. 여기에서 편히 쉬며 체력을 회복할 수 있습니다."],
    1: ["[묘지]", "묘지는 조용하고 무서운 곳입니다. 차가운 바람이 지나가며, 누군가가 당신을 지켜보고 있는 듯한 기분이 듭니다. 이곳에서는 과거의 영웅들과 전설에 관한 이야기를 찾을 수 있습니다."],
    2: ["[힐러집]", "힐러집은 고요하고 평온한 분위기가 감돌고 있습니다. 아름다운 정원과 진한 약초 냄새가 전해집니다. 상처와 질병을 치료할 수 있는 강력한 마법사들이 이곳에서 봉사하고 있습니다."],
    3: ["[잡화점]", "잡화점에는 세상의 다양한 물건들이 가득합니다. 이곳에서는 모험에 필요한 도구와 장비를 구입할 수 있습니다. 사장님이 항상 밝은 얼굴로 인사해주며, 고객들과 이야기를 나누고 있습니다."],
    4: ["[은행근처]", "은행 근처는 번화가의 중심입니다. 사람들이 북적이며, 거리에는 상인들이 자신의 물품을 파는 노점도 있습니다. 이곳에서는 자금을 관리하거나 소중한 물건을 보관할 수 있습니다."],
    5: ["[목축지]", "목축지는 푸른 초원과 넓은 들판이 펼쳐져 있는 곳입니다. 소와 양 등의 가축들이 평화롭게 먹이를 찾고 있습니다. 이곳에서는 소박한 농부들과 함께 일하며, 농작물과 가축에 대한 지식을 얻을 수 있습니다."],
    6: ["[대장간]", "대장간에서는 불꽃이 튀기며 철과 강철이 녹아내립니다. 대장장이가 망치질하며, 새로운 무기와 갑옷을 만들고 있습니다. 이곳에서는 전투에 필요한 강력한 무기와 방어구를 살 수 있습니다"]
}

actions = ["[전투]",
           "[전체 스킬 확인]",
           "[인벤토리 확인]",
           "[캐릭터 정보 확인]",
           "[장착한 스킬 확인]",
           "[장착한 장비 확인]",
           "[캐릭터 변경]",
           "[뒤로가기]"
           ]


def staging(mainState):
    stage_num = mainState.stage
    place_select, place_subscript = list(zip(*places.values()))
    print(place_subscript[stage_num])
    input(" ")
    action_value, action_index = pick(
        selection, f"{place_subscript[stage_num]}\n{mainState.propname}이 할 행동은?")

    # 이동 선택지 고를시
    if action_index == 0:
        move_value, move_index = pick(place_select, "이동하고 싶은 장소를 선택해주세요")
        print(f'{move_value.strip("[,]").strip(" ")}로 이동합니다\n')
        os.system('cls')
        return move_index
    # 행동 선택지 고를시
    else:
        action_value, action_index = pick(
            actions, f'{place_select[stage_num].strip("[]")} {mainState.propname}은 지금 무엇을 하나요?')
        action_function[action_index](mainState)
        return stage_num


def script_controller(script):
    for i in range(0, len(script)):
        os.system('cls')
        print('\n'+script[i]+('\n'*5))
        input('엔터를 눌러주세요.')


def new_game():
    # 이름입력
    os.system('cls')
    u_name = input('당신의 이름은 무엇인가요?')
    # 직업선택
    _,u_class_select = pick(scripts.u_class,'직업을 선택하세요',)
    # 스토리텔링
    script_controller(scripts.u_story)
    return u_name , str(u_class_select)

# # class Battle:
#     # 전투준비
# def new_battle(self):
#     print('전투가 시작됨'+('\n'*5))
#     # 전투
#     print('전투중'+('\n'*5))

# def my_turn(self):
#     u_battle_select = select_display('당신의 턴',scripts.u_battle)

# def end_battle(self):
#     # 전투결과
#     print('전투가 끝났습니다. 당신은 ~~~ 얻었습니다.')

# # 전투속행 질의
# u_battel_end = select_display('다음전투를 계속 하시겠습니까?',scripts.u_continue_select)
# # 종료

# # 인벤토리
# u_equip = select_display('어떤 장비를 착용합니까?',scripts.u_equip_list)
# u_inventory = select_display('어떤 아이템을 착용합니까?',scripts.u_inventory_list)

# a = ''
