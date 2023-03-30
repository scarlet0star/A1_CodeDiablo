import random
from itertools import zip_longest
from textcolor import *

# ***************** 나중에 구현할 것들 ******************
# 크리티컬 데미지
#     연금술
#     마법
# 스킬 범위 공격
# 턴 우선권(무게)
# 칭호

# 전투 구현 파일입니다.
# 최소 1 : 1 전투에서 최대 1 : 4 까지 구현 할 예정
# 스킬이 1개만 타깃

# main이나 스크린이나 스테이지에서....
# 데이터 map.json에서 맵의 monster 들을 불러온다. (맵마다 monster 출몰이 다르기 때문에...)
# 데이터 character.json에서 player와 확정숫자 or 랜덤으로(1~4) 만큼 monster들을 불러온다.


# 상태 를 보여준다
#
# 입력 값을 받아 (일반공격, 스킬공격, 물약먹기, 도망가기) 선택한다.
#
# player가 monster를 공격할 때
# max_att = [(캐릭터스탯+아이템스탯)*4 + 무기공격력or마법공격력] * player의 캐릭에 따라 스킬계수(1 if 일공)
# damage = max(round(max_att*0.8, max_att) - 상대 방어구 방어 능력치, 0)
#
# player battle_max_hp = hp + (캐릭터스탯+아이템스탯)*50 + 아이템hp
#
# skill을 썼다면 skill의 경험치를 올려준다.
# skill의 경험치로 레벨업이 되었으면
#   -skill을 업데이트하고 skill.json도 업데이트한다.
#
# 타겟의 battle_max_hp -= damage
#
# 피해 정보를 보여준다
# 데미지가 0일 경우 miss를 보여준다.
# 아군과 적 상태를 보여준다.
#
# Player가 죽었으면
#   - 전투 종료
#   - 마을에서 다시 태어나기
#   (hp, mp는 각 max의 10%로... 경험치도 80% 하락, character.json에 업데이트)
#
# 적이 죽었으면 경험치를 얻는다.
#
# 남아 있는 적이 있으면 Player를 공격한다.
# max_att = [(캐릭터스탯+아이템스탯)*4 + 무기공격력or마법공격력] * player의 캐릭에 따라 스킬계수(1 if 일공)
# damage = max(round(max_att*0.8, max_att) - 상대 방어구 방어 능력치, 0)
# 데미지가 0일 경우 miss를 보여준다.
# monster battle_max_hp = hp + (캐릭터스탯+아이템스탯)*50 + 아이템hp
#
# 타겟의 battle_max_hp -= damage
#
# 피해 정보를 보여준다
# 데미지가 0일 경우 miss를 보여준다.
# 아군과 적 상태를 보여준다.
#
# (추후) 여러 마리일 경우 또 계산해야함. monster1, monster2....
# ********** 반복 *****************
#
#
# battle 종료시
# player의 경험치를 얻고
# player가 레벨업을 하면
#   - hp, mp를 풀 회복해준다. 추가 스탯?
# player만 character.json에 업데이트 한다.


# 전투의 룰은 다음과 같습니다.
# player가 공격을 하고
# monster 수 만큼 각각 공격하고...

class Battle:
    # player의 능력과 enemy의 능력을 가져오는 함수?
    def __init__(self, player_character, enemy_character):
        self.battle_round = 1  # ??????
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

        action_list = []
        for speed in range(enemy.speed):
            available_card = random.choice(
                [card for card in hand if card.action <= enemy.action])
            action_list.append(available_card)
            hand.remove(available_card)
            graveyard.append(available_card)

        return action_list

    # 전투 바로 직전 무조건 실행할 함수
    def start(self):
        # hp표시
        # 상대 표시
        pass

        # # 전투 최초 시작시 일어날 일, 추후 계획에 따라 더 추가될 여지 있음
        # # 플레이어와 적이 모두 카드를 3장씩 뽑습니다.
        # self.draw_cards(self.player_character, self.player_hand,        # 아직 사용 용도를 정하지 않음...
        #                 self.player_graveyard, 3)

        # self.draw_cards(self.enemy_character, self.enemy_hand,          # 아직 사용 용도를 정하지 않음...
        #                 self.enemy_graveyard, 3)

    def round_start(self):
        # 매 라운드 시작시 마다 일어날 로직을 작성합니다.
            self.enemy_character, self.enemy_hand, self.enemy_graveyard)

# 플레이어의 행동을 배치하는 로직입니다.
# 임시 패와 무덤을 생성하여 플레이어에게 confirm할 여지를 줬습니다.
# zip_longest를 이용하여 무대응시 혹은 초기 대응시에 대한 작업을 했지만 무대응의 경우 구현이 더 필요합니다.
# validation의 경우 user의 input이 현재 가지고 있는 핸드에 맞는지, action 소모량을 넘지 않는지 확인합니다.
# => action 포인트가 부족한 경우, 무대응을 하도록 해야하는데 무대응에 대한 구현이 아직 부족합니다.
# confirm 여부에 따라 temp를 비우거나 혹은 현대 패 상태에 temp를 적용합니다.

    def player_attack(self, skill_name):       # Player가 enemy를 공격하는 함수
        # if 스킬0번째 있는 거냐? >> 일반 공격인지 묻는 거임.
            # print("일반공격입니다.")
            # damage_per = 1
        # else:
            # print('스킬 공격이구나?')
            # skill 의 계수를 가져오기
            # damage_per

        # if hits 수가 for문 동안 반복해서 때린다.

        weapon=self.player_character.Equip.used_item_list["무기"]

        # 크리티컬은 독립 수행
        # player_character._luck 값에 따라 크리티컬 발생 확률이 달라짐
        critical_chance=self.player_character._luck / 500

        # 0부터 1 사이의 난수 생성
        rand_num=random.random()

        # 크리 유무
        critical_YN=False
        if rand_num < critical_chance:
            # 크리티컬 발생
            print("크리티컬!")
            critical_YN=True
            damage_per += 1.6

        if (self.player_character._classname == "전사"):
            main_stat_sum=self.player_character._str * 4

            max_att=(main_stat_sum + 무기_물리_공격력) * damage_per
            damage=max(random.randint(round(max_att * 0.8, max_att)
                       ) - self.enemy_character._physical_defense, 0)

        elif (self.player_character._classname == "궁수"):
            main_stat_sum=self.player_character._dex * 4

            max_att=(main_stat_sum + 무기_물리_공격력) * damage_per
            damage=max(random.randint(round(max_att * 0.8, max_att)
                       ) - self.enemy_character._physical_defense, 0)

        elif (self.player_character._classname == "마법사"):
            main_stat_sum=self.player_character._int * 4

            max_att=(main_stat_sum + 무기_마법_공격력) * damage_per
            damage=max(random.randint(round(max_att * 0.8, max_att)
                       ) - self.enemy_character._magic_defense, 0)
        elif (self.player_character._classname == "연금술사"):
            main_stat_sum=self.player_character._max_hp + \
                self.player_character._max_mp  # ???????????????

            max_att=(main_stat_sum + 무기_물리_공격력) * damage_per
            damage=max(random.randint(round(max_att * 0.8, max_att)
                       ) - self.enemy_character._physical_defense, 0)
        else:
            # print("뭐야? 잡캐야?")
            # 모든 스탯 히든???? 누가 어떤 스킬이 더 쎌 지 모름 ㅋㅋㅋ
            main_stat_sum=self.player_character._str + self.player_character._dex + \
                self.player_character._int + self.player_character._will + self.player_character._luck
            damage=max(random.randint(round(max_att * 0.8, max_att)
                       ) - self.enemy_character._physical_defense, 0)

        self.enemy_character -= damage

        # 크리티컬이면 데미지를 노란색으로
        # 데미지가 0일 경우 MISS를 보여준다.
        if damage != 0:
            if critical_YN == True:
                print(f"{Colors.GREEN}{self.name}{Colors.RESET}의 공격! {Colors.RED}{self.enemy_character._name}{Colors.RESET}에게 {Colors.YELLOW}{damage}{Colors.RESET}을(를) 입혔습니다.")
            else:
                print(
                    f"{Colors.GREEN}{self.name}{Colors.RESET}의 공격! {Colors.RED}{self.enemy_character._name}{Colors.RESET}에게 {damage}을(를) 입혔습니다.")
        else:
            print(f"{Colors.GREEN}{self.name}{Colors.RESET}의 공격! {Colors.RED}{self.enemy_character._name}{Colors.RESET}에게 MISS")




    def enemy__attack(self, skill_name):    # name이든 뭐든 어떻든 써서
        # if 스킬0번째 있는 거냐? >> 일반 공격인지 묻는 거임.
            # print("일반공격입니다.")
            # damage_per = 1
        # else:
            # print(skill_name)
            # skill 의 계수를 가져오기
            # damage_per

        # player_character._luck 값에 따라 크리티컬 발생 확률이 달라짐
        critical_chance=self.player_character._luck / 500

        # 0부터 1 사이의 난수 생성
        rand_num=random.random()

        # 크리 유무
        critical_YN=False
        if rand_num < critical_chance:
            # 크리티컬 발생
            print("크리티컬!")
            critical_YN=True
            damage_per += 1.6

        if (self.player_character._classname == "전사"):
            main_stat_sum=self.player_character._str * 4

            max_att=(main_stat_sum + 무기_물리_공격력) * damage_per
            damage=max(random.randint(round(max_att * 0.8, max_att)
                       ) - self.enemy_character._physical_defense, 0)

        elif (self.player_character._classname == "궁수"):
            main_stat_sum=self.player_character._dex * 4

            max_att=(main_stat_sum + 무기_물리_공격력) * damage_per
            damage=max(random.randint(round(max_att * 0.8, max_att)
                       ) - self.enemy_character._physical_defense, 0)

        elif (self.player_character._classname == "마법사"):
            main_stat_sum=self.player_character._int * 4

            max_att=(main_stat_sum + 무기_마법_공격력) * damage_per
            damage=max(random.randint(round(max_att * 0.8, max_att)
                       ) - self.enemy_character._magic_defense, 0)
        elif (self.player_character._classname == "연금술사"):
            main_stat_sum=self.player_character._max_hp + \
                self.player_character._max_mp  # ???????????????

            max_att=(main_stat_sum + 무기_물리_공격력) * damage_per
            damage=max(random.randint(round(max_att * 0.8, max_att)
                       ) - self.enemy_character._physical_defense, 0)
        else:
            # 잡캐 or 적의 스탯
            # print("뭐야? 잡캐야?")
            # 모든 스탯 히든???? 누가 어떤 스킬이 더 쎌 지 모름 ㅋㅋㅋ
            main_stat_sum=self.player_character._str + self.player_character._dex + \
                self.player_character._int + self.player_character._will + self.player_character._luck
            damage=max(random.randint(round(max_att * 0.8, max_att)
                       ) - self.enemy_character._physical_defense, 0)

        self.enemy_character -= damage

        # 크리티컬이면 데미지를 노란색으로
        # 데미지가 0일 경우 MISS를 보여준다.
        # 나중엔 스킬이름을 넣으면 된다....
        if damage != 0:
            if critical_YN == True:
                print(f"{Colors.RED}{self.name}{Colors.RESET}의 공격! {Colors.GREEN}{self.enemy_character._name}{Colors.RESET}에게 {Colors.YELLOW}{damage}{Colors.RESET}을(를) 입혔습니다.")
            else:
                print(
                    f"{Colors.RED}{self.name}{Colors.RESET}의 공격! {Colors.GREEN}{self.enemy_character._name}{Colors.RESET}에게 {damage}을(를) 입혔습니다.")
        else:
            print(f"{Colors.RED}{self.name}{Colors.RESET}의 공격! {Colors.GREEN}{self.enemy_character._name}{Colors.RESET}에게  MISS")


# 위력을 비교하는 함수입니다. randint를 통해 무작위 변수를 생성해 위력을 결정하고 비교합니다.
# 위력이 쎈 쪽이 상대방에게 데미지를 입힙니다.

    # 공격하고 받는 그런?

# 배틀 상황에 대한 전개입니다.
# 클래스에서 정의된 모든 함수들이 여기서 사용됩니다.
# 마지막에 미리 백업해둔 캐릭터 데이터를 통해 캐릭터를 복구하고 main stage(3)으로 갑니다.

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
                f'{Colors.GREEN}일반공격{Colors.RESET}(\"1\"), {Colors.BLUE}스킬공격{Colors.RESET}(\"2\"), ', end = "")
            # 미구현?
            print(
                f'{Colors.ORANGE}물약먹기{Colors.RESET}(\"3\"), {Colors.RED}도망가기{Colors.RESET}(\"4\")')
            print(f'게임종료(\"any key\") 미구현?')
            user_input=str(
                input(f"\n>>입력: "))

            if user_input == "1":
                self.player_attack(skill_name=0???)
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
                    self.player_character.hp=self.player_character.max_hp=self.backup.hp  # 다음 레벨의 hp
                    self.player_character.mp=self.player_character.max_mp=self.backup.mp
                    self.player_character.lv += 1
                    self.player_character.exp=0
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
                self.player_character.hp=round(
                    10 * self.player_character.hp/self.player_character.max_hp)
                # 10%의 마나로 부활하게...
                self.player_character.mp=round(
                    10 * self.player_character.mp/self.player_character.max_mp)
                break
                # self.enemy_skill_attack()

            print(f"\n{self.battle_round}라운드 종료!\n")
            self.battle_round += 1

        # 캐릭터 백업용
        # self.player_character = self.backup

        return 3
