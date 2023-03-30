# from battle import Battle
# from character import Character
# from main import create_card_instance, enemies
from pick import pick
from os import system
import scripts

# # # 게임시작
# items = k,v keys= k values = v

# # 스테이지 넘버를 받아 특정 스테이지의 텍스트를 출력합니다.
# # return으로 해당 stage의 선택지 텍스트를 리턴합니다.
# stage_num -> stage[stage_num] stage_text => "환영합니다~~" "1 ㅁㅁㅁ 2 ㅁㅁㅁ"

def screen_output(stage_num):   # 스테이지 넘버를 받아옴 
    stage_text = stage[stage_num]   
    return stage_text["select"]


# # 시작 스테이지의 선택지 로직입니다. 선택지 로직은 보통 스테이지 넘버를 리턴합니다.

def start_stage():
    u_menu_select = select_display(scripts.SCRIPT_TEXT_NEW_GAME_TITLE_0_0, scripts.u_new_game)
    if u_menu_select == 2:
        exit(0)
    return u_menu_select

# def start_stage(choice, mainState):
#     if choice == 1:
#         return "캐릭터이름변경"
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


# def e_select_display(insert_scription,insert_selector):
    
#     script = insert_scription
#     select = insert_selector

#     out_selector, index = pick(select, script)
    
#     # print(index, out_selector)
#     return index

# def main_menu():
#     # 1. 새겜 2.불러오기 3.겜 종료
#     while True:
#         u_main = e_select_display(scripts.SCRIPT_TEXT_NEW_GAME_TITLE_0_0, scripts.u_new_game)
#         if u_main == 0:
#             return new_game()
#         elif u_main == 1:
#             continue
#         else:
#             exit()

# def e_battle():
#     pass

# while True:
#     break


stage_diction = {
    "광장":{
        "desciption":"여기는 광장, 무엇을 하지?",
                    #특정 위치로 이동하는 선택지, #특정 행동을 하는 선택지
        "select":["~~로 이동","자기","인벤토리 열어보기","클래스 변경"]
    },
    "광장2":{
        "desciption":"여기는 광장, 무엇을 하지?",
        "select":["자기","인벤토리 열어보기","클래스 변경"]
    },
    "광장3":{
        "desciption":"여기는 광장, 무엇을 하지?",
        "select":["자기","인벤토리 열어보기","클래스 변경"]
    },
                 }




selection = ["이동","행동"]

places = ["[ 여관(저장) ]",
         "[ 묘지 ]",
         "[ 힐러집 ]",
         "[ 잡화점 ]",
         "[ 은행근처(전투) ]",
         "[ 목축지(전투) ]",
         "[ 대장간 ]",
         "현재 위치",
         "[ 다른곳으로 이동 ]"]

actions = ["전투",
           "전체 스킬 확인",
           "인벤토리 확인",
           "캐릭터 정보 확인",
           "장착한 장비 확인",
           "캐릭터 변경",
           "[뒤로가기]"
           ]

def battle_stage():
    #전투 시작?
    pass
def view_skill():
    # 스킬 확인
    pass
def view_inventory():
    # 인벤토리 확인
    pass
def view_status():
    # 스테이터스 확인
    pass
def view_equip():
    # 인벤토리 확인
    pass
def change_char():
    # 캐릭터 선택
    pass
def back():
    pass

print('')


action_function = {0:battle_stage,
                   1:view_skill,
                   2:view_inventory,
                   3:view_status,
                   4:view_equip,
                   5:change_char,
                   6:back,}

moving_function = {0:hotel,
                   1:cemetry,
                   2:healerhouse,
                   3:store,
                   4:bank,
                   5:land,
                   6:fergus,
                   7:diff,} 
    
places = ["[ 여관(저장) ]",
         "[ 묘지(전투) ]",
         "[ 힐러집 ]",
         "[ 잡화점 ]",
         "[ 은행근처(전투) ]",
         "[ 목축지(전투) ]",
         "[ 대장간 ]",
         "[ 다른곳으로 이동 ]"]

def stage(stage_num):
    description = stage_diction[stage_num]["description"]
    
    action_value,action_index = pick(selection,description)
    # 이동 선택지 고를시
    if action_value == "[ 여관(저장) ]":
        move_value,move_index = pick(places,"")
        return move_index
    # 행동 선택지 고를시
    else:
        action_value, action_index = pick(actions,"")
        action_function[action_index](self.mainState)
        return stage_num



# def select_display("현재 스테이지 키"):
#     현재 스테이지 설명 = stage_diction["현재 스테이지 키"]["description"]
#     (현재 스테이지 등장 선택지) = stage_diction["현재 스테이지 키"]["select"]
#     print(현재 스테이지 설명)
    
#     text = screen_output(mainState.stage)
    
    
#     select = get_user_input(text)
    
#     select를 받는 과정 = 선택지를 출력해서 어떤 행동을 할지 물어봄
    
#     pick은 여기서 씀
    
#     <next_stage = stage.get(mainState.stage).get("logic")(select, mainState)>
    
#     [이동] [행동]
    
#     [] [] [] []
    
#     특정위치 도착:
#     print("아 여기 여관이지...")
    
#     [행동]
#     [장비확인], [스킬보기], [전투]
#     ->
#     리턴 제자리 위치 
    
#     스타트 -> 특정 위치로 떨어질거 -> 1. 이동 : 0(여관) : 여관에 대한 스크립트가 출력됨 -> 1.이동 2.행동 
#     로드
#     종료
    
#     맵에 있다면
#     1. 이동 -> 이동할 곳 선택지 출력
    
#      {
#         0 : "[ 여관(저장) ]",
#         1 : "[ 묘지 ]",
#         2 : "[ 힐러집 ]",
#         3 : "[ 잡화점 ]",
#         4 : "[ 은행근처(전투) ]",
#         5 : "[ 목축지(전투) ]",
#         6 : "[ 대장간 ]",
#         7 : "현재 위치:",
#         8 : "[ 다른곳으로 이동 ]"
#         }
#     2. 행동 -> 행동할 것 선택지 출력
#         1. 전투
#         2. 장비
#         3. 스텟확인
#         4. 게임끄기
        
#     if 특정 행동을 실행하는 선택지:
#         main_state.change_character()
#         "특정 로직을 실행함"
#         return 특정 위치로 이동하는 키값(보통= 현재위치)
#     else(다른 장소로 이동만 하는 선택지):

#         return 픽을 통해 받은 선택지 키값
    
    
    
    
    script = insert_scription
    select = insert_selector

    out_selector, index = pick(select, script)
    
    # print(index, out_selector)
    return "다음 스테이지 키"


def scription_controller(scription):
    for i in range(0,len(scription)):
        system('cls')
        print('\n'+scription[i]+('\n'*5))
        input('엔터를 눌러주세요.')


    
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
    
def end_battle(self):
    # 전투결과
    print('전투가 끝났습니다. 당신은 ~~~ 얻었습니다.')
    
# 전투속행 질의
u_battel_end = select_display('다음전투를 계속 하시겠습니까?',scripts.u_continue_select)
# 종료  

# 인벤토리
u_equip = select_display('어떤 장비를 착용합니까?',scripts.u_equip_list)
u_inventory = select_display('어떤 아이템을 착용합니까?',scripts.u_inventory_list)

a = ''
