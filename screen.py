from battle import Battle
from character import Character
<<<<<<< Updated upstream
from main import create_card_instance, enemies

# 만약 여유가 있다면 텍스트는 따로 저장할 예정입니다.

start = '''김성광의 게임에 오신것을 환영합니다.\n캐릭터를 생성하거나 기존에 생성한 캐릭터를 통해 몬스터와 전투를 할 수 있습니다.'''

start_select = ["[ 캐릭터 생성하기 ]",
                "[ 캐릭터 불러오기 ]",
                "[ 게임 종료하기 ]"]

character_gen = "생성하고 싶은 캐릭터의 이름을 정해주세요."

load = "기존에 생성한 캐릭터를 불러오고 있습니다."

main = "메인 화면입니다. 하고 싶은 활동을 선택해주세요"

main_select = ["[ 장비 확인하기 ]",
               "[ 캐릭터 확인하기 ]",
               "[ 콜로세움으로 진입 ]",
               "[ 게임 종료하기 ]",]

battle = "콜로세움에 오신 것을 환영합니다. 상대할 적을 골라주세요."

battle_select = ["[ 고통스러워 하는 개발자 ]",
                 "[ 비슷한 상대 ]"]


# 스테이지 넘버를 받아 특정 스테이지의 텍스트를 출력합니다.
# return으로 해당 stage의 선택지 텍스트를 리턴합니다.

def screen_output(stage_num):
    stage_text = stage[stage_num]
    print(stage_text["text"] if stage_text["text"] != None else "")

    return stage_text["select"]

# 리턴된 선택지 리스트를 받아와서 하나씩 출력합니다.유저의 input을 리턴받습니다. 
# 이때 리스트 혹은 문자열 판별을 isinstance를 이용합니다. 이후 출력을 따로 받습니다.

def get_user_input(select):
    if isinstance(select, list):
        for i, choice in enumerate(select):
            print(f"{i + 1} | {choice}")
        user_input = int(input("\n원하는 선택지는? >> "))

    elif isinstance(select, str) and select == "input":
        user_input = input("\n값을 기입해주세요 >> ")

    else:
        user_input = ""

    return user_input

# 시작 스테이지의 선택지 로직입니다. 선택지 로직은 보통 스테이지 넘버를 리턴합니다.

def start_stage(choice, mainState):
    if choice == 1:
        return 1
    elif choice == 2:
        return 2
    elif choice == 3:
        exit()
    else:
        print("선택지에 없는 입력을 하셨습니다. 다시 선택해주세요.")


def gen_stage(choice, mainState):
    mainState.user.name = choice

    print(f"\n환영합니다 {choice}!")
    print("캐릭터를 성공적으로 생성했습니다. 이제 게임으로 진입합니다.\n")
    return 3


def load_stage(choice, mainState):
    # json 형태로 저장할 세이브 파일을 불러오는 코드입니다. 예정사항
    print("미구현 입니다.")
    return 3


def main_stage(choice, mainState):
    if choice == 1:
        return 5
    elif choice == 2:
        return 4
    elif choice == 3:
        return 6
    elif choice == 4:
        exit()
    else:
        print("잘못된 값을 입력하셨습니다.\n")


def character_info(choice, mainState):
    print(mainState.user)
    return 3


def equip_info(choice, mainState):
    print(mainState.user.equip)
    return 3

# main.py에서 적을 생성하기 힘들어서 stage.py에서 선택지에 따라 적도 생성합니다
# 적을 생성한 이후 전투로 넘어갑니다. battle이 끝나면 다시 메인 선택지(3)으로 넘어갑니다.

def battle_stage(choice, mainState):
    enemy = Character(card_instances=create_card_instance(
        False), **enemies[str(choice)])

    battle = Battle(mainState.user, enemy)
    battle.battle(mainState.user, enemy)
    return 3

# 스테이지 정보를 담고있는 딕셔너리입니다. logic에 함수를 담아 main.py에서 불러올 수 있습니다.
# python에서는 함수 역시 1급 객체이기에 가능한 일입니다. 

stage = {
    0: {"text": start,
        "select": start_select,
        "logic": start_stage},
    1: {"text": character_gen,
        "select": "input",
        "logic": gen_stage},
    2: {"text": load,
        "select": None,
        "logic": load_stage},
    3: {"text": main,
        "select": main_select,
        "logic": main_stage
        },
    4: {"text": None,
        "select": "",
        "logic": character_info
        },
    5: {"text": None,
        "select": "",
        "logic": equip_info
        },
    6: {"text": battle,
        "select": battle_select,
        "logic": battle_stage
        }
}
# from battle import Battle
# from character import Character
# from main import create_card_instance, enemies

# # 만약 여유가 있다면 텍스트는 따로 저장할 예정입니다.

# start = '''김성광의 게임에 오신것을 환영합니다.\n캐릭터를 생성하거나 기존에 생성한 캐릭터를 통해 몬스터와 전투를 할 수 있습니다.'''

# start_select = ["[ 캐릭터 생성하기 ]",
#                 "[ 캐릭터 불러오기 ]",
#                 "[ 게임 종료하기 ]"]

# character_gen = "생성하고 싶은 캐릭터의 이름을 정해주세요."

# load = "기존에 생성한 캐릭터를 불러오고 있습니다."

# main = "메인 화면입니다. 하고 싶은 활동을 선택해주세요"

# main_select = ["[ 장비 확인하기 ]",
#                "[ 캐릭터 확인하기 ]",
#                "[ 콜로세움으로 진입 ]",
#                "[ 게임 종료하기 ]",]

# battle = "콜로세움에 오신 것을 환영합니다. 상대할 적을 골라주세요."

# battle_select = ["[ 고통스러워 하는 개발자 ]",
#                  "[ 비슷한 상대 ]"]


# # 스테이지 넘버를 받아 특정 스테이지의 텍스트를 출력합니다.
# # return으로 해당 stage의 선택지 텍스트를 리턴합니다.

# def screen_output(stage_num):
#     stage_text = stage[stage_num]
#     print(stage_text["text"] if stage_text["text"] != None else "")

#     return stage_text["select"]

# # 리턴된 선택지 리스트를 받아와서 하나씩 출력합니다.유저의 input을 리턴받습니다. 
# # 이때 리스트 혹은 문자열 판별을 isinstance를 이용합니다. 이후 출력을 따로 받습니다.

# def get_user_input(select):
#     if isinstance(select, list):
#         for i, choice in enumerate(select):
#             print(f"{i + 1} | {choice}")
#         user_input = int(input("\n원하는 선택지는? >> "))

#     elif isinstance(select, str) and select == "input":
#         user_input = input("\n값을 기입해주세요 >> ")

#     else:
#         user_input = ""

#     return user_input

# # 시작 스테이지의 선택지 로직입니다. 선택지 로직은 보통 스테이지 넘버를 리턴합니다.

# def start_stage(choice, mainState):
#     if choice == 1:
#         return 1
#     elif choice == 2:
#         return 2
#     elif choice == 3:
#         exit()
#     else:
#         print("선택지에 없는 입력을 하셨습니다. 다시 선택해주세요.")


# def gen_stage(choice, mainState):
#     mainState.user.name = choice

#     print(f"\n환영합니다 {choice}!")
#     print("캐릭터를 성공적으로 생성했습니다. 이제 게임으로 진입합니다.\n")
#     return 3


# def load_stage(choice, mainState):
#     # json 형태로 저장할 세이브 파일을 불러오는 코드입니다. 예정사항
#     print("미구현 입니다.")
#     return 3


# def main_stage(choice, mainState):
#     if choice == 1:
#         return 5
#     elif choice == 2:
#         return 4
#     elif choice == 3:
#         return 6
#     elif choice == 4:
#         exit()
#     else:
#         print("잘못된 값을 입력하셨습니다.\n")


# def character_info(choice, mainState):
#     print(mainState.user)
#     return 3


# def equip_info(choice, mainState):
#     print(mainState.user.equip)
#     return 3

# # main.py에서 적을 생성하기 힘들어서 stage.py에서 선택지에 따라 적도 생성합니다
# # 적을 생성한 이후 전투로 넘어갑니다. battle이 끝나면 다시 메인 선택지(3)으로 넘어갑니다.

# def battle_stage(choice, mainState):
#     enemy = Character(card_instances=create_card_instance(
#         False), **enemies[str(choice)])

#     battle = Battle(mainState.user, enemy)
#     battle.battle(mainState.user, enemy)
#     return 3

# # 스테이지 정보를 담고있는 딕셔너리입니다. logic에 함수를 담아 main.py에서 불러올 수 있습니다.
# # python에서는 함수 역시 1급 객체이기에 가능한 일입니다. 

# stage = {
#     0: {"text": start,
#         "select": start_select,
#         "logic": start_stage},
#     1: {"text": character_gen,
#         "select": "input",
#         "logic": gen_stage},
#     2: {"text": load,
#         "select": None,
#         "logic": load_stage},
#     3: {"text": main,
#         "select": main_select,
#         "logic": main_stage
#         },
#     4: {"text": None,
#         "select": "",
#         "logic": character_info
#         },
#     5: {"text": None,
#         "select": "",
#         "logic": equip_info
#         },
#     6: {"text": battle,
#         "select": battle_select,
#         "logic": battle_stage
#         }
# }



def select_display(insert_scription,insert_selector):
    from pick import pick
    script = insert_scription
    select = insert_selector

    out_selector, index = pick(select, script)
    
    print(index, out_selector)
    return index, out_selector


# mi = display('김첨지는 맛좋은 김치',['설렁탕','막걸리','팥빙수'])

# print(mi[0])



import scripts
from os import system
# 게임시작
new_game = [
            scripts.SCRIPT_TEXT_NEW_GAME_1_1,
            scripts.SCRIPT_TEXT_NEW_GAME_1_2,
            scripts.SCRIPT_TEXT_NEW_GAME_1_3,
            ]
u_class = [scripts.SCRIPT_TEXT_SELECT_USER_CLASS_WARRIOR,
           scripts.SCRIPT_TEXT_SELECT_USER_CLASS_WIZARD,
           scripts.SCRIPT_TEXT_SELECT_USER_CLASS_ARCHER,
           scripts.SCRIPT_TEXT_SELECT_USER_CLASS_ALCHEMIST]
u_story = [scripts.SCRIPT_TEXT_PROLOGUE_0_0,
           scripts.SCRIPT_TEXT_PROLOGUE_0_1,
           scripts.SCRIPT_TEXT_PROLOGUE_0_2]

u_battle = ['일반공격','스킬','도망치기']

u_continue_select = [scripts.SCRIPT_TEXT_YES,
                     scripts.SCRIPT_TEXT_NO]

def scription_controller(scription):
    for i in range(0,len(scription)):
        system('cls')
        print('\n'+scription[i]+('\n'*5))
        input('엔터를 눌러주세요.')
        
    

u_menu_select = select_display(scripts.SCRIPT_TEXT_NEW_GAME_TITLE_0_0, new_game)
# 이름입력
system('cls') 
name = input('당신의 이름은 무엇인가요?')
# 직업선택
u_class_select = select_display('직업을 선택하세요',u_class)
# 스토리텔링
scription_controller(u_story)
# 전투준비
print('전투가 시작됨'+('\n'*5))
# 전투
print('전투중'+('\n'*5))
battle_select = select_display('당신의 턴',u_battle)
# 전투결과
print('전투가 끝났습니다. 당신은 ~~~ 얻었습니다.')
# 전투속행 질의
battel_end = select_display('다음전투를 계속 하시겠습니까?',u_continue_select)
# 종료
=======
from main import enemies, characters
import os
import scripts
from utils import pick, load_files
from time import sleep
from main import create_card_instance, enemies
from main import Player

items = load_files('item.json')


def script_controller(script):
    for i in range(0, len(script)):
        os.system('cls')
        print('\n'+script[i]+('\n'*5))
        a = input('엔터를 눌러주세요.')
        sleep(3)


def battle_stage(mainState):
    enemy_cha = Character(**characters["1"])
    enemy = Player(**{"propname": "마법사",
                      "user": enemy_cha})
    battle = Battle(mainState, enemy)
    battle.battle()
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


def potion_store(mainState):
    from item import Potion

    item_key = items["물약"]
    new_potion = Potion(**item_key)                   # 포션 인스턴스 생성

    script_controller(scripts.n_potion)  # 힐러집 대사

    u_potion_cnt = len(mainState._equip.get_potion_list())
    store_porion_list = ["물약", "[나가기]", "현재 물약 개수 : "+str(u_potion_cnt)]
    n_script = ['마누스 : 필요한 물건을 골라봐.', '마누스 : 더 필요한건 없어?.']
    n_num = 0

    while True:

        u_select, u_index = pick(
            store_porion_list, n_script[n_num])         # 선택지 생성

        if u_select == "물약":
            u_potion_cnt = len(mainState._equip.get_potion_list())
            mainState._equip.add_item(new_potion)  # 캐릭터에 포션 넘기기
            store_porion_list.pop(2)
            store_porion_list.append("현재 물약 개수 : "+str(u_potion_cnt))
        n_num = 1
        if u_select == "[나가기]":
            return mainState.stage


# potion_store(0)

def armory(mainState):
    from random import randint
    import item
    script_controller(scripts.n_armor)  # 대장간 대사

    armor_key = items["방어구"]                        # 장비류 인스턴스 생성
    wep_key = items["무기"]
    armor = item.Arms(**armor_key)
    wep = item.Arms(**wep_key)

    store_porion_list = ["무기", "방어구", "[나가기]"]
    n_script = ['퍼거스 : 무기를 고치러 왔나?',
                '퍼거스 : 이크! 손이 미끄러졌네... 헐...', "네가 내 운을 다 빨아먹어서 실패한 거야!"]
    n_num = 0
    while True:

        u_select, u_index = pick(store_porion_list, n_script[n_num])  # 선택지생성

        if u_select == "방어구":
            mainState._equip.add_item(armor)
            n_num = randint(1, 2)
        elif u_select == "무기":
            mainState._equip.add_item(wep)
        if u_select == "[나가기]":
            return mainState.stage
# armory(0)


def grocery_store(mainState):
    script_controller(
        ["잡화점에는 세상의 다양한 물건들이 가득합니다. 이곳에서는 모험에 필요한 도구와 장비를 구입할 수 있습니다. 사장님이 항상 밝은 얼굴로 인사해주며, 고객들과 이야기를 나누고 있습니다."])


def bank(mainState):
    script_controller(
        ["은행 근처는 번화가의 중심입니다. 사람들이 북적이며, 거리에는 상인들이 자신의 물품을 파는 노점도 있습니다. 이곳에서는 자금을 관리하거나 소중한 물건을 보관할 수 있습니다."])


def hotel(mainState):
    script_controller(
        ["여관에서는 다양한 모험가들이 쉬고 있습니다. 따뜻한 분위기와 향긋한 음식 냄새가 흐릅니다. 여기에서 편히 쉬며 체력을 회복할 수 있습니다."])


def grave(mainState):
    script_controller(
        ["묘지는 조용하고 무서운 곳입니다. 차가운 바람이 지나가며, 누군가가 당신을 지켜보고 있는 듯한 기분이 듭니다. 이곳에서는 과거의 영웅들과 전설에 관한 이야기를 찾을 수 있습니다."])


def field(mainState):
    script_controller(
        ["목축지는 푸른 초원과 넓은 들판이 펼쳐져 있는 곳입니다. 소와 양 등의 가축들이 평화롭게 먹이를 찾고 있습니다. 이곳에서는 소박한 농부들과 함께 일하며, 농작물과 가축에 대한 지식을 얻을 수 있습니다."])

# grocery_store(0)


action_function = {0: battle_stage,
                   1: view_skill,
                   2: view_inventory,
                   3: view_status,
                   4: view_used_skill,
                   5: view_equip,
                   6: change_char,
                   7: back, }

selection = ["이동", "행동"]

p_actions = [
    "[여관]",
    "[묘지]",
    "[힐러집]",
    "[잡화점]",
    "[은행근처]",
    "[목축지]",
    "[대장간]",
]

p_action_function = {0: hotel,
                     1: grave,
                     2: potion_store,
                     3: grocery_store,
                     4: bank,
                     5: field,
                     6: armory,
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
    place_select, place_subscript = p_actions, p_action_function
    action_value, action_index = pick(
        selection, f"{place_select[stage_num]}\n{mainState.propname}이 할 행동은?")

    # 이동 선택지 고를시
    if action_index == 0:
        move_value, move_index = pick(place_select, "이동하고 싶은 장소를 선택해주세요")
        print(f'{place_select[move_index]}로 이동합니다\n')
        p_action_function[move_index](mainState)
        return move_index
    # 행동 선택지 고를시
    else:
        action_value, action_index = pick(
            actions, f'{place_select[stage_num].strip("[]")} {mainState.propname}은 지금 무엇을 하나요?')
        action_function[action_index](mainState)
        return stage_num


def new_game():
    # 이름입력
    os.system('cls')
    u_name = input('당신의 이름은 무엇인가요?')
    # 직업선택
    _, u_class_select = pick(scripts.u_class, '직업을 선택하세요')
    # 스토리텔링
    script_controller(scripts.u_story)
    return u_name, str(u_class_select+1)

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
>>>>>>> Stashed changes
