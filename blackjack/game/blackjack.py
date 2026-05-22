import random
import time
from src.utils import clearConsole
from src.database import saveUserInfo

def create_deck():
    suits = ['♠', '◆', '♥', '♣']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [f"{suit}{rank}" for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def calculate_score(hand):
    score = 0
    aces = 0
    for card in hand:
        rank = card[1:]
        if rank in ['J', 'Q', 'K']:
            score += 10
        elif rank == 'A':
            aces += 1
            score += 11
        else:
            score += int(rank)
            
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
    return score

def play_blackjack(userInfo):
    clearConsole()

    if userInfo["coin"] <= 0:
        print("\n[!] 보유 코인이 부족합니다.")
        input("\n엔터를 누르면 돌아갑니다.")
        return
    
    print("┌───────────────────────────────────┐")
    print("  블랙잭 테이블에 입장하셨습니다.")
    print(f"  COIN: {userInfo['coin']:,}")
    print("└───────────────────────────────────┘")

    while True:
        try:
            bet = int(input("배팅 > "))
            if 1 <= bet <= userInfo["coin"]:
                break
            print(f"1 ~ {userInfo['coin']}코인까지 배팅 가능합니다.")
        except ValueError:
            print("올바른 숫자를 입력해 주세요.")

    deck = create_deck()
    dealer_card = [deck.pop(), deck.pop()]
    player_card = [deck.pop(), deck.pop()]

    clearConsole()

    while True:
        clearConsole()
        player = calculate_score(player_card)

        dealer_cards_str = f"[{dealer_card[0]}] [?]"
        player_cards_str = " ".join(f"[{card}]" for card in player_card)

        print("┌───────────────────────────────────┐")
        print(f"  DEALER  ▶  {dealer_cards_str}")
        print(f"          └─ Score: ?")
        print(f"  PLAYER  ▶  {player_cards_str}")
        print(f"          └─ Score: {player}")
        print(f"  BETTING: {bet:,}")
        print("└───────────────────────────────────┘")

        if player >= 21:
            break

        choice = input(
            "\n [1] Hit  [2] Stand\n > "
        )

        if choice == "1":
            player_card.append(deck.pop())
        elif choice == "2":
            break
    
    player = calculate_score(player_card)

    if player <= 21:
        clearConsole()

        current_dealer_cards = [dealer_card[0], dealer_card[1]]
        dealer_cards_str = " ".join(f"[{card}]" for card in current_dealer_cards)
        dealer = calculate_score(current_dealer_cards)

        print("┌───────────────────────────────────┐")
        print(f"  DEALER  ▶  {dealer_cards_str} ⮜ 오픈!")
        print(f"          └─ Score: {dealer}")
        print(f"  PLAYER  ▶  {player_cards_str}")
        print(f"          └─ Score: {player}")
        print(f"  BETTING: {bet:,}")
        print("└───────────────────────────────────┘")
        time.sleep(1.2)

        while calculate_score(dealer_card) < 17:
            new_card = deck.pop()
            dealer_card.append(new_card)
            dealer = calculate_score(dealer_card)
            dealer_cards_str = " ".join(f"[{card}]" for card in dealer_card)
            
            clearConsole()
            print("┌───────────────────────────────────┐")
            print(f"  DEALER  ▶  {dealer_cards_str} + 추가!")
            print(f"          └─ Score: {dealer}")
            print(f"  PLAYER  ▶  {player_cards_str}")
            print(f"          └─ Score: {player}")
            print(f"  BETTING: {bet:,}")
            print("└───────────────────────────────────┘")
            time.sleep(1.2)
    
    # --- 3. 최종 결과 정산 화면 ---
    dealer = calculate_score(dealer_card)
    final_dealer_cards = " ".join(f"[{card}]" for card in dealer_card)
    final_player_cards = " ".join(f"[{card}]" for card in player_card)
    
    clearConsole()
    print("┌───────────────────────────────────┐")
    print(f"   DEALER  ▶  {final_dealer_cards}")
    print(f"           └─ Score: {dealer}")
    print(f"   PLAYER  ▶  {final_player_cards}")
    print(f"           └─ Score: {player}")
    print(f"   BETTING ▶  {bet:,}")
    print("└───────────────────────────────────┘")
    
    print()
    if player > 21:
        print(f" [ 패배 ] {player}, 버스트 (-{bet:,})")
        userInfo["coin"] -= bet
        userInfo["loss"] += 1
    elif dealer > 21:
        print(f" [ 승리 ] {dealer}, 버스트 (+{bet:,})")
        userInfo["coin"] += bet
        userInfo["win"] += 1
    elif player > dealer:
        print(f" [ 승리 ] +{bet:,}")
        userInfo["coin"] += bet
        userInfo["win"] += 1
    elif player < dealer:
        print(f" [ 패배 ] -{bet:,}")
        userInfo["coin"] -= bet
        userInfo["loss"] += 1
    else:
        print(" [ 무승부 ]")
        userInfo["draw"] += 1

    saveUserInfo(userInfo)
    print(f" [ 잔액 ] {userInfo['coin']:,}")
    input("\n엔터를 누르면 메인으로 돌아갑니다.")
