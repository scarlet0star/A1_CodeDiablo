# from battle import Battle
# from character import Character
# from main import create_card_instance, enemies
from pick import pick
from os import system
import scripts

# # # 게임시작



# # 스테이지 넘버를 받아 특정 스테이지의 텍스트를 출력합니다.
# # return으로 해당 stage의 선택지 텍스트를 리턴합니다.

# def screen_output(stage_num):   # 스테이지 넘버를 받아옴 
#     stage_text = stage[stage_num]   
#     return stage_text["select"]

#     # items = k,v keys= k values = v
    

# # 시작 스테이지의 선택지 로직입니다. 선택지 로직은 보통 스테이지 넘버를 리턴합니다.

# def start_stage(mainState):
#     u_menu_select = select_display(scripts.SCRIPT_TEXT_NEW_GAME_TITLE_0_0, scripts.u_new_game)
#     if u_menu_select == 2:
#         exit(0)
#     return u_menu_select

# def gen_stage(choice, mainState):
#     mainState.user.name = choice

#     print(f"\n환영합니다 {choice}!")
#     print("캐릭터를 성공적으로 생성했습니다. 이제 게임으로 진입합니다.\n")
#     return 3


# def load_stage(choice, mainState):
#     # json 형태로 저장할 세이브 파일을 불러오는 코드입니다. 예정사항
#     print("미구현 입니다.")
#     return 3


# def main_stage(mainState):
#     choice = select_display()
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
#     0: {"select": start_stage},
#     1: {"text": scripts.SCRIPT_TEXT_CREATE_USER,
#         "select": "input",
#         "logic": gen_stage},
#     # 2: {"text": load,
#     #     "select": None,
#     #     "logic": load_stage},
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
    
    script = insert_scription
    select = insert_selector

    out_selector, index = pick(select, script)
    
    # print(index, out_selector)
    return index


def scription_controller(scription):
    for i in range(0,len(scription)):
        system('cls')
        print('\n'+scription[i]+('\n'*5))
        input('엔터를 눌러주세요.')

def main_menu():
    # 1. 새겜 2.불러오기 3.겜 종료
    u_main = select_display(scripts.SCRIPT_TEXT_NEW_GAME_TITLE_0_0, scripts.u_new_game)
    if u_main == 0:
        new_game()
    elif u_main == 1:
        pass
    else:
        exit()
    
def new_game():
    # 이름입력
    system('cls') 
    u_name = input('당신의 이름은 무엇인가요?')
    # 직업선택
    u_class_select = select_display('직업을 선택하세요',scripts.u_class)
    # 스토리텔링
    scription_controller(scripts.u_story)
    return u_name , u_class_select

# class Battle:
    # 전투준비
def new_battle(self):
    print('전투가 시작됨'+('\n'*5))
    # 전투
    print('전투중'+('\n'*5))
    
def my_turn(self):
    u_battle_select = select_display('당신의 턴',scripts.u_battle)
    
def 

# 전투결과
print('전투가 끝났습니다. 당신은 ~~~ 얻었습니다.')
# 전투속행 질의
u_battel_end = select_display('다음전투를 계속 하시겠습니까?',scripts.u_continue_select)
# 종료  

# 인벤토리
u_equip = select_display('어떤 장비를 착용합니까?',scripts.u_equip_list)
u_inventory = select_display('어떤 아이템을 착용합니까?',scripts.u_inventory_list)

a = ''