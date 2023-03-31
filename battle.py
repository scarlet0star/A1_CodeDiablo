import random
from itertools import zip_longest
from textcolor import *


class Battle:
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
        status += f"체력: {you._hp}/{you._max_hp}\n"

        # HP bar
        if 0.5 <= per_hp <= 1:
            status += f"{Colors.BLUE}{you._name}{Colors.RESET}의 상태: {Colors.RED} HP {Colors.RESET}{Colors.GREEN}{you.hp}{Colors.RESET}/{Colors.GREEN}{you.max_hp}{Colors.RESET}, {Colors.BLUE}MP {you.mp}{Colors.RESET}/{Colors.BLUE}{you.max_mp}{Colors.RESET}"
            status += f"{Colors.GREEN}░{Colors.RESET}" * \
                left_hp + "░" * (50 - left_hp)
        elif 0.2 <= per_hp < 0.5:
            status += f"{Colors.BLUE}{you._name}{Colors.RESET}의 상태: {Colors.RED} HP {Colors.RESET}{Colors.ORANGE}{you.hp}{Colors.RESET}/{Colors.GREEN}{you.max_hp}{Colors.RESET}, {Colors.BLUE}MP {you.mp}{Colors.RESET}/{Colors.BLUE}{you.max_mp}{Colors.RESET}"
            status += f"{Colors.ORANGE}░{Colors.RESET}" * \
                left_hp + "░" * (50 - left_hp)
        else:
            status += f"{Colors.BLUE}{you._name}{Colors.RESET}의 상태: {Colors.RED} HP {Colors.RESET}{Colors.RED}{you.hp}{Colors.RESET}/{Colors.GREEN}{you.max_hp}{Colors.RESET}, {Colors.BLUE}MP {you.mp}{Colors.RESET}/{Colors.BLUE}{you.max_mp}{Colors.RESET}"
            status += f"{Colors.RED}░{Colors.RESET}" * \
                left_hp + "░" * (50 - left_hp)

        # MP bar
        status += f"{Colors.BLUE}░{Colors.RESET}" * \
            left_mp + "░" * (50 - left_mp)

        # EXP bar
        status += f"{Colors.YELLOW}░{Colors.RESET}" * \
            left_exp + "░" * (50 - left_exp)

        return status

        # 캐릭터 스크린이 있지 않나?

    def class_att(self, damage_per):

        weapon = self.player_character.Equip.used_item_list["무기"]

        if (self.player_character._classname == "전사"):
            main_stat_sum = self.player_character._str * 4

            max_att = (main_stat_sum + weapon._dmg) * damage_per
            damage = max(random.randint(round(max_att * 0.8, max_att)
                                        ) - self.enemy_character._def, 0)

        elif (self.player_character._classname == "궁수"):
            main_stat_sum = self.player_character._dex * 4

            max_att = (main_stat_sum + weapon._dmg) * damage_per
            damage = max(random.randint(round(max_att * 0.8, max_att)
                                        ) - self.enemy_character._def, 0)

        elif (self.player_character._classname == "마법사"):
            main_stat_sum = self.player_character._int * 4

            max_att = (main_stat_sum + weapon._magicdmg) * damage_per
            damage = max(random.randint(round(max_att * 0.8, max_att)
                                        ) - self.enemy_character._def, 0)
        elif (self.player_character._classname == "연금술사"):
            main_stat_sum = self.player_character._max_hp + \
                self.player_character._max_mp  # ???????????????

            max_att = (main_stat_sum + weapon._dmg) * damage_per
            damage = max(random.randint(round(max_att * 0.8, max_att)
                                        ) - self.enemy_character._def, 0)
        else:
            # 잡캐 or 몬스터
            # print("뭐야? 잡캐야?")
            # 모든 스탯 히든???? 누가 어떤 스킬이 더 쎌 지 모름 ㅋㅋㅋ
            main_stat_sum = self.player_character._str + self.player_character._dex + \
                self.player_character._int + self.player_character._will + self.player_character._luck
            damage = max(random.randint(round(max_att * 0.8, max_att)
                                        ) - self.enemy_character._physical_defense, 0)
        return damage

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
            # 크리티컬은 독립 수행
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
            att_print = f"{Colors.GREEN}{self.name}{Colors.RESET}의 공격! {Colors.RED}{self.enemy_character._name}{Colors.RESET}에게 "
            if damage != 0:
                if critical_YN == True:
                    att_print += f"{Colors.YELLOW}{damage}{Colors.RESET}을(를) 입혔습니다."
                else:
                    att_print += f"{damage}을(를) 입혔습니다."
            else:
                att_print += f"MISS"

            print(att_print)

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

            print(att_print)

    def battle(self, player, enemy):    # 배틀이 시작되는 첫 함수

        # self.start()

        # 여기서 로직....
        while player.hp > 0 and enemy.hp > 0:
            # 아군 상태를 보여주는 함수
            print(self.show_status(player))
            # 적 상태를 보여주는 함수
            print(self.show_status(enemy))

            print(f'{self.battle_round}라운드가 시작되었습니다\n')  # 1 라운드가 1턴 인가?

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
                    # self.player_character.max_exp += ???

                # 아이템?
                # character.json에 저장하기??? save에?
                break
            else:
                # 에너미가 스킬이 있다면 먼저 쓰기?? 랜덤으로 뭐할지.... 알아서 계산 해서
                self.enemy_pysical_attack()

            # 아군 상태를 보여주는 함수
            print(self.show_status(player))
            # 적 상태를 보여주는 함수
            print(self.show_status(enemy))

            if self.player_character.hp <= 0:
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

            print(f"\n{self.battle_round}라운드 종료!\n")
            self.battle_round += 1

        # 캐릭터 백업용
        # self.player_character = self.backup

        return 3
