import random
from itertools import zip_longest

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
    def __init__(self, player_character, enemy_character):
        self.battle_round = 1
        self.player_character = player_character
        self.enemy_character = enemy_character

        self.player_hand = []
        self.player_graveyard = []
        self.enemy_hand = []
        self.enemy_graveyard = []

        self.player_actions = []
        self.enemy_actions = []

        self.backup = player_character

    def draw_cards(self, character, hand, graveyard, nums=1):
        # 카드를 뽑기. 덱과 핸드, 무덤의 카드 수를 비교하여 세 리스트 사이에서 카드를 서로 옮깁니다.
        deck = character.equip.card_list
        max_val = character.equip.max
        # 카드 드로우는 한번씩 진행됩니다. 덱이 비어있다면 무덤을 비우고 덱으로 채웁니다.
        for draw_count in range(nums):
            if len(deck) - 1 < 0:
                print("덱이 비었기에 무덤의 카드를 다시 덱으로 불러옵니다\n")
                deck = graveyard[::]
                graveyard.clear()
            if len(hand) < max_val:
                draw = random.choice(deck)
                deck.remove(draw)
                hand.append(draw)
            else:
                print("핸드가 가득찼기에 카드를 뽑지 않습니다.\n")

    # 적의 카드 배치를 하는 함수입니다. 사용가능한 카드 중에서 랜덤으로 하나를 골라 배치합니다.

    def enemy_place_card(self, enemy, hand, graveyard):
        action_list = []
        for speed in range(enemy.speed):
            available_card = random.choice(
                [card for card in hand if card.action <= enemy.action])
            action_list.append(available_card)
            hand.remove(available_card)
            graveyard.append(available_card)

        return action_list

    def start(self):
        # 전투 최초 시작시 일어날 일, 추후 계획에 따라 더 추가될 여지 있음
        # 플레이어와 적이 모두 카드를 3장씩 뽑습니다.
        self.draw_cards(self.player_character, self.player_hand,
                        self.player_graveyard, 3)
        self.draw_cards(self.enemy_character, self.enemy_hand,
                        self.enemy_graveyard, 3)

    def round_start(self):
        # 매 라운드 시작시 마다 일어날 로직을 작성합니다.
        # 플레이어와 적이 모두 카드를 1장씩 뽑고 action 2를 받습니다.

        self.player_character.action += 2
        self.enemy_character.action += 2

        self.draw_cards(self.player_character,
                        self.player_hand, self.player_graveyard)
        self.draw_cards(self.enemy_character,
                        self.enemy_hand, self.enemy_graveyard)

        self.enemy_actions = self.enemy_place_card(
            self.enemy_character, self.enemy_hand, self.enemy_graveyard)

# 플레이어의 행동을 배치하는 로직입니다.
# 임시 패와 무덤을 생성하여 플레이어에게 confirm할 여지를 줬습니다.
# zip_longest를 이용하여 무대응시 혹은 초기 대응시에 대한 작업을 했지만 무대응의 경우 구현이 더 필요합니다.
# validation의 경우 user의 input이 현재 가지고 있는 핸드에 맞는지, action 소모량을 넘지 않는지 확인합니다.
# => action 포인트가 부족한 경우, 무대응을 하도록 해야하는데 무대응에 대한 구현이 아직 부족합니다.
# confirm 여부에 따라 temp를 비우거나 혹은 현대 패 상태에 temp를 적용합니다.

    def player_setting(self):
        print("\n적이 아래와 같이 공격합니다. 어떻게 대응하나요?")

        temp_actions = []
        temp_graveyard = []
        temp_hand = self.player_hand[::]
        temp_action_points = self.player_character.action

        while True:

            for my_attack, ene_attack in zip_longest(temp_actions, self.enemy_actions, fillvalue="empty"):
                print(f'>>>>> {my_attack} vs {ene_attack} <<<<<')

            print("\n현재 패에 아래와 같은 카드가 있습니다")
            print("카드명 / 액션소모 / 카드 값 / 특수 효과")
            for idx, card in enumerate(self.player_hand, start=1):
                print(f'{idx} : {card}')

            player_choice = int(input(
                f"대응할 카드 번호를 입력해주세요 : 현재 배치 가능 갯수 / 액션 포인트 : ({self.player_character.speed} / {self.player_character.action}) "))

            while True:
                if 1 <= player_choice <= len(temp_hand):
                    selected_card = temp_hand[player_choice - 1]
                    if temp_action_points >= selected_card.action:
                        temp_actions.append(selected_card)

                        temp_hand.remove(selected_card)
                        temp_graveyard.append(selected_card)
                        temp_action_points -= selected_card.action
                        break
                    else:
                        print("액션 포인트가 부족합니다.\n")
                else:
                    print("잘못된 입력입니다.\n")

            if self.player_character.speed == len(temp_actions) or temp_action_points <= 0:
                print(
                    f"\n액션 포인트 소모량 : {self.player_character.action - temp_action_points}")
                for my_attack, ene_attack in zip_longest(temp_actions, self.enemy_actions, fillvalue="empty"):
                    print(f'>>>>> {my_attack} vs {ene_attack} <<<<<')

                confirm = input("\n선택한 카드로 진행하시겠습니까? (1: 예, 0: 아니오) ")

                if confirm == "1":
                    self.player_actions = temp_actions
                    self.player_graveyard = temp_graveyard
                    self.player_hand = temp_hand[::]
                    self.player_character.action = temp_action_points
                    break
                elif confirm == "0":
                    temp_actions = []
                    temp_graveyard = []
                    temp_hand = self.player_hand[::]
                    temp_action_points = self.player_character.action

# 위력을 비교하는 함수입니다. randint를 통해 무작위 변수를 생성해 위력을 결정하고 비교합니다.
# 위력이 쎈 쪽이 상대방에게 데미지를 입힙니다.

    def after_setting(self):
        for player_card, enemy_card in zip(self.player_actions, self.enemy_actions):
            player_damage = self.player_character.power + \
                random.randint(player_card.minV, player_card.maxV)
            enemy_damage = self.enemy_character.power + \
                random.randint(enemy_card.minV, enemy_card.maxV)

        print(f"\n플레이어 스킬의 위력 : {player_damage} vs 적 스킬의 위력 {enemy_damage}!!")
        if player_damage > enemy_damage:
            self.enemy_character.hp -= player_damage
            print(
                f"{self.player_character.name}이(가) {self.enemy_character.name}에게 {player_damage}의 데미지를 입혔습니다.")
        elif enemy_damage > player_damage:
            self.player_character.hp -= enemy_damage
            print(
                f"{self.enemy_character.name}이(가) {self.player_character.name}에게 {enemy_damage}의 데미지를 입혔습니다.")
        else:
            print("두 캐릭터의 데미지가 동일하여 아무런 피해도 입히지 못했습니다.")

# 배틀 상황에 대한 전개입니다.
# 클래스에서 정의된 모든 함수들이 여기서 사용됩니다.
# 마지막에 미리 백업해둔 캐릭터 데이터를 통해 캐릭터를 복구하고 main stage(3)으로 갑니다.

    def battle(self, player, enemy):

        self.start()

        while player.hp > 0 and enemy.hp > 0:
            player_status = str(player).split('\n')
            enemy_status = str(enemy).split('\n')

            print(f'{self.battle_round}라운드가 시작되었습니다\n')
            print("플레이어 상태 vs 적 상태")
            for p_line, e_line in zip(player_status, enemy_status):
                print(f"{p_line:<25} {e_line}")

            self.round_start()
            self.player_setting()
            self.after_setting()
            print("\n라운드 종료! 액션 포인트가 2씩 증가합니다.\n")
            self.battle_round += 1

            if self.player_character.hp <= 0:
                print("\n패배 했습니다...\n")
            elif self.enemy_character.hp <= 0:
                print("\n승리!\n")

        self.player_character = self.backup

        return 3
