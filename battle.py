import random
from itertools import zip_longest
from textcolor import *


class Battle():
    # player의 능력과 enemy의 능력을 가져오는 함수?
    def __init__(self, player_character, enemy_character):
        self.battle_round = 1
        self.player_character = player_character
        self.enemy_character = enemy_character

        self.backup = player_character  # 저장 용도

    # you의 상태를 보여주는 함수
    def show_status(you):
        per_hp = you.hp/you.max_hp
        per_mp = you.mp/you.max_mp
        per_exp = you.exp/you.max_exp
        left_hp = round(per_hp * 50)
        left_mp = round(per_mp * 50)
        left_exp = round(per_exp * 50)

        status = f"캐릭터 클래스: {you._classname}\n"
        status += f"레벨: {you._lv}\n\n"
        # HP bar
        status += f"체력: {you._hp}/{you._max_hp}\n"
        status += f"{Colors.YELLOW}{you._propname}{Colors.RESET}의 상태: {Colors.RED} HP {Colors.RESET}"
        if 0.5 <= per_hp <= 1:
<<<<<<< Updated upstream
            status += f"{Colors.BLUE}{you._name}{Colors.RESET}의 상태: {Colors.RED} HP {Colors.RESET}{Colors.GREEN}{you.hp}{Colors.RESET}/{Colors.GREEN}{you.max_hp}{Colors.RESET}, {Colors.BLUE}MP {you.mp}{Colors.RESET}/{Colors.BLUE}{you.max_mp}{Colors.RESET}"
            status += f"{Colors.GREEN}░{Colors.RESET}" * \
                left_hp + "░" * (50 - left_hp)
        elif 0.2 <= per_hp < 0.5:
            status += f"{Colors.BLUE}{you._name}{Colors.RESET}의 상태: {Colors.RED} HP {Colors.RESET}{Colors.ORANGE}{you.hp}{Colors.RESET}/{Colors.GREEN}{you.max_hp}{Colors.RESET}, {Colors.BLUE}MP {you.mp}{Colors.RESET}/{Colors.BLUE}{you.max_mp}{Colors.RESET}"
            status += f"{Colors.ORANGE}░{Colors.RESET}" * \
                left_hp + "░" * (50 - left_hp)
        else:
            status += f"{Colors.BLUE}{you._name}{Colors.RESET}의 상태: {Colors.RED} HP {Colors.RESET}{Colors.RED}{you.hp}{Colors.RESET}/{Colors.GREEN}{you.max_hp}{Colors.RESET}, {Colors.BLUE}MP {you.mp}{Colors.RESET}/{Colors.BLUE}{you.max_mp}{Colors.RESET}"
=======
            status += f"{Colors.GREEN}{you._hp}{Colors.RESET}/{Colors.GREEN}{you._max_hp}{Colors.RESET}, {Colors.BLUE}MP {you._mp}{Colors.RESET}/{Colors.BLUE}{you._max_mp}{Colors.RESET}"
            status += f"{Colors.GREEN}░{Colors.RESET}" * \
                left_hp + "░" * (50 - left_hp)
        elif 0.2 <= per_hp < 0.5:
            status += f"{Colors.ORANGE}{you._hp}{Colors.RESET}/{Colors.GREEN}{you._max_hp}{Colors.RESET}, {Colors.BLUE}MP {you._mp}{Colors.RESET}/{Colors.BLUE}{you._max_mp}{Colors.RESET}"
            status += f"{Colors.ORANGE}░{Colors.RESET}" * \
                left_hp + "░" * (50 - left_hp)
        else:
            status += f"{Colors.RED}{you._hp}{Colors.RESET}/{Colors.GREEN}{you._max_hp}{Colors.RESET}, {Colors.BLUE}MP {you._mp}{Colors.RESET}/{Colors.BLUE}{you._max_mp}{Colors.RESET}"
>>>>>>> Stashed changes
            status += f"{Colors.RED}░{Colors.RESET}" * \
                left_hp + "░" * (50 - left_hp)

        # MP bar
        status += f"마나: {you._mp}/{you._max_mp}\n"
        status += f"{Colors.BLUE}░{Colors.RESET}" * \
            left_mp + "░" * (50 - left_mp)

        # EXP bar
        status += f"EXP: {you._exp}/{you._max_exp}\n"
        status += f"{Colors.GREEN}░{Colors.RESET}" * \
            left_exp + "░" * (50 - left_exp)

        print(status)

    def class_att(self, me, target, damage_per):

        # weapon = self.player_character.Equip.used_item_list["무기"]
        weapon = me.Equip.used_item_lsit["무기"]

        if (me._classname == "전사"):
            main_stat_sum = me._str * 4

            max_att = (main_stat_sum + weapon._dmg) * damage_per
            damage = max(random.randint(round(max_att * 0.8, max_att)
                                        ) - target._def, 0)

        elif (me._classname == "궁수"):
            main_stat_sum = me._dex * 4

            max_att = (main_stat_sum + weapon._dmg) * damage_per
            damage = max(random.randint(round(max_att * 0.8, max_att)
                                        ) - target._def, 0)

        elif (me._classname == "마법사"):
            main_stat_sum = me._int * 4

            max_att = (main_stat_sum + weapon._magicdmg) * damage_per
            damage = max(random.randint(round(max_att * 0.8, max_att)
<<<<<<< Updated upstream
                                        ) - self.enemy_character._def, 0)
        elif (self.player_character._classname == "연금술사"):
            main_stat_sum = self.player_character._max_hp + \
                self.player_character._max_mp  # ???????????????
=======
                                        ) - target._def, 0)
        elif (me._classname == "연금술사"):
            main_stat_sum = me._max_hp + \
                me._max_mp
>>>>>>> Stashed changes

            max_att = (main_stat_sum + weapon._dmg) * damage_per
            damage = max(random.randint(round(max_att * 0.8, max_att)
                                        ) - target._def, 0)
        else:
            main_stat_sum = me._str + me._dex + \
                me._int + me._will + me._luck
            damage = max(random.randint(round(max_att * 0.8, max_att)
                                        ) - target._physical_defense, 0)
        return damage

<<<<<<< Updated upstream
    def player_attack(self, skill_name):       # Player가 enemy를 공격하는 함수
        # if 스킬0번째 있는 거냐? >> 일반 공격인지 묻는 거임.
        # print("일반공격입니다.")
        # damage_per = 1
        # else:
        # print('스킬 공격이구나?')
        # skill 의 계수를 가져오기
        # damage_per

        # hits 수가 for문 동안 반복해서 때린다.
        for i in skill._hits:
=======
    def attack(self, me, target, skill):       # me가 target을 공격
        # select_skill = self.player_character._equip._used_skill_list[skill]
        select_skill = me._equip._used_skill_list[skill]

        print(select_skill._name)  # 스킬의 이름이 출력

        damage_per = 1
        if select_skill._name == "일반 공격":
            # 계수를 곱하지 않음
            pass
        else:
            # 스킬 사용
            # skill의 계수를 가져온다.
            damage_per *= select_skill._damage_per

        # skill의 hits 수가 for문 동안 반복해서 때린다.
        for i in select_skill._hits:
>>>>>>> Stashed changes
            # 크리티컬은 독립 수행
            # player_character._luck 값에 따라 크리티컬 발생 확률이 달라짐
            critical_chance = me._luck / 500

            # 0부터 1 사이의 난수 생성
            rand_num = random.random()

            # 크리 유무
            critical_YN = False
            if rand_num < critical_chance:
                # 크리티컬 발생
                print("크리티컬!")
                critical_YN = True
                damage_per += 1.6

            damage = self.class_att(self, me, target, damage_per)

            # 적에게 데미지를 넣음
            target.hp -= damage

            # 데미지를 입힌 프린트
            # 크리티컬이면 데미지를 노란색으로
            # 데미지가 0일 경우 MISS를 보여준다.
<<<<<<< Updated upstream
            att_print = f"{Colors.GREEN}{self.name}{Colors.RESET}의 공격! {Colors.RED}{self.enemy_character._name}{Colors.RESET}에게 "
=======
            att_print = f"{Colors.GREEN}{me._name}{Colors.RESET}의 공격! {Colors.RED}{target._name}{Colors.RESET}에게 "
>>>>>>> Stashed changes
            if damage != 0:
                if critical_YN == True:
                    att_print += f"{Colors.YELLOW}{damage}{Colors.RESET}을(를) 입혔습니다."
                else:
                    att_print += f"{damage}을(를) 입혔습니다."
            else:
                att_print += f"MISS"

            print(att_print)
<<<<<<< Updated upstream

        def enemy_attack(self, skill_name):    # name이든 뭐든 어떻든 써서
            # if 스킬0번째 있는 거냐? >> 일반 공격인지 묻는 거임.
            # print("일반공격입니다.")
            # damage_per = 1
            # else:
            # print(skill_name)
            # skill 의 계수를 가져오기
            # damage_per

            # player_character._luck 값에 따라 크리티컬 발생 확률이 달라짐
            critical_chance = self.player_character._luck / 500

            # 0부터 1 사이의 난수 생성
            rand_num = random.random()

            # 크리 유무
            critical_YN = False
            if rand_num < critical_chance:
                # 크리티컬 발생
                print("크리티컬!")
                critical_YN = True
                damage_per += 1.6

            damage = self.class_att()

            self.enemy_character -= damage

            # 크리티컬이면 데미지를 노란색으로
            # 데미지가 0일 경우 MISS를 보여준다.
            att_print = f"{Colors.RED}{self.name}{Colors.RESET}의 공격! {Colors.GREEN}{self.enemy_character._name}{Colors.RESET}에게 "
            if damage != 0:
                if critical_YN == True:
                    att_print += f"{Colors.YELLOW}{damage}{Colors.RESET}을(를) 입혔습니다."
                else:
                    att_print += f"{damage}을(를) 입혔습니다."
            else:
                att_print += f"MISS"
=======

    # 상태를 표현하는 함수
    def status(self, player, enemy):
        # 아군 상태를 보여주는 함수
        print(self.show_status(player))
        # 적 상태를 보여주는 함수
        print(self.show_status(enemy))

###############################################################################################################
# 전투시 선택창

    def battle_selector(self):
        u_skill = self.player_character._equip.print_total_skill_list()     # 스킬리스트 할당
        # [공격] [물약] [도주]
        # [공격1] [공격2] [공격3]

        # 공격 할 지 물약을 사용할지 선택
        i = input('0. 공격 1. 물약')
        # 입력 받음

        # a. 공격을 할 경우
        if i == 0:
            for idx, val in enumerate(u_skill, 0):
                print(str(idx)+', '+str(val))       # 스킬리스트 출력
            # A. 일반공격 0
            # B. 스킬1  1
            # C. 스킬22
            j = input('사용할 스킬을 입력하세요:')
            if j > len(u_skill):
                j = input('다시입력하세요: ')
            else:
                return int(j)
        # b. 물약을 마실경우
        elif i == 1:
            x = input('생명력 50 포션을 마셨다! [ 엔터<< ]')
            self.player_character.use_item()
            print(self.player_character)
            return str('a')  # 물약을 마심

    # 리턴 타입은 str, skill 몇 번째인지(0= 일반공격, 1)
####################################################################################################################
>>>>>>> Stashed changes

            print(att_print)

    def battle(self, player, enemy):    # 배틀이 시작되는 첫 함수

<<<<<<< Updated upstream
        # self.start()

        # 여기서 로직....
        while player.hp > 0 and enemy.hp > 0:
            # 아군 상태를 보여주는 함수
            print(self.show_status(player))
            # 적 상태를 보여주는 함수
            print(self.show_status(enemy))
=======
        player_character = self.player_character.character
        enemy_character = self.enemy_character.character
        # self.start()

        # 여기서 로직....
        while player_character._hp > 0 and enemy_character._hp > 0:

            # round 시작전 상태 보여주는 함수
            self.status(player_character, enemy_character)
>>>>>>> Stashed changes

            print(f'{self.battle_round}라운드가 시작되었습니다\n')  # 1 라운드가 1턴 인가?
            # 라운드 시작
            # 공격 물약
            # -------------------------------- 플레이어 턴 시작---------------------------------
            skill = self.battle_selector()
            if skill != 'a':
                self.attack(self, player_character, enemy_character, skill)

<<<<<<< Updated upstream
            # 내가 먼저 턴 쓰는.... 나중에 if문으로든 해서 럭이든 무게든 써서 턴....
            # pick으로 구현하기??????
            print(
                f'{Colors.GREEN}일반공격{Colors.RESET}(\"1\"), {Colors.BLUE}스킬공격{Colors.RESET}(\"2\"), ', end="")
            # 미구현?
            print(
                f'{Colors.ORANGE}물약먹기{Colors.RESET}(\"3\"), {Colors.RED}도망가기{Colors.RESET}(\"4\")')
            print(f'게임종료(\"any key\") 미구현?')
            user_input = str(
                input(f"\n>>입력: "))

            if user_input == "1":
                self.enemy_attack(skill_name=0???)
                # 일반공격
            elif user_input == "2":
                # 스킬공격
                # 가지고 있는 skill 뜨게 하기
                # 그 중에 스킬 선택을 해서
                self.player_attack(skill_name???)
            elif user_input == "3":
                print("물약먹기, 턴을 소비?")
            elif user_input == "4":  # 미구현?
                print("도망가셨습니다. 미구현?")
                break
            else:
                print("게임종료 미구현?")
                break
                # exit()
            # self.round_start()

            # 그래픽이든 뭐든 때리는 소리와 그래픽을????

            # enemy1이 0 이하라면
            if (self.enemy_character.hp <= 0):
                print("\n승리!\n")
                # 보상 받는 것!
                # 경험치
                self.player_character.exp += self.enemy_character.exp
                if (self.player_character.exp >= self.enemy_character.max_exp):
                    print("레벨업하셨습니다!")
                    self.player_character.hp = self.player_character.max_hp = self.backup.hp  # 다음 레벨의 hp
                    self.player_character.mp = self.player_character.max_mp = self.backup.mp
                    self.player_character.lv += 1
                    self.player_character.exp = 0
=======
            if (enemy_character._hp <= 0):  # enemy1이 0 이하라면 #
                print("\n승리!\n")
                # 보상 받는 것!
                # 경험치
                player_character._exp += enemy_character._exp
                if (player_character._exp >= enemy_character._max_exp):
                    print("레벨업!")
                    player_character._hp = player_character._max_hp = self.backup.character._hp  # 다음 레벨의 hp
                    player_character._mp = player_character._max_mp = self.backup.character._mp
                    player_character._lv += 1
                    player_character._exp = 0
>>>>>>> Stashed changes
                    # self.player_character.max_exp += ???

                break
<<<<<<< Updated upstream
            else:
                # 에너미가 스킬이 있다면 먼저 쓰기?? 랜덤으로 뭐할지.... 알아서 계산 해서
                self.enemy_pysical_attack()

            # 아군 상태를 보여주는 함수
            print(self.show_status(player))
            # 적 상태를 보여주는 함수
            print(self.show_status(enemy))

            if self.player_character.hp <= 0:
=======
            # -------------------------------- 몬스터 턴 시작 ---------------------------------
            # 플레이어 턴 후 상태 보여주는 함수
            self.status(player_character, enemy_character)

            # 플레이어의 hp 가 0 이하라면
            if player_character._hp <= 0:
>>>>>>> Stashed changes
                print("\n패배 했습니다...\n")
                print("\n마을에서 부활합니다.\n")
                # 10%의 체력으로 부활하게...
                self.player_character.hp = round(
                    10 * self.player_character.hp/self.player_character.max_hp)
                # 10%의 마나로 부활하게...
                self.player_character.mp = round(
                    10 * self.player_character.mp/self.player_character.max_mp)
                break
                # self.enemy_skill_attack()
            else:
                # 랜덤 초이스 스킬?
                self.attack(self, enemy_character,
                            player_character, random.randint(1, 4))
            # -------------------------------- 몬스터 턴 끝 ---------------------------------
                print(f"\n{self.battle_round}라운드 종료!\n")
                self.battle_round += 1

        return 3
