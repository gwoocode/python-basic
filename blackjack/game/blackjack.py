import random
from src.utils import clearConsole
from src.database import saveUserInfo

def create_deck():
    suits = ['♠', '◆', '♥', '♣']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [f"{suit}{rank}" for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def calculate_score(card):
    rank = card[1:]
    values = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return values[rank] if rank in values else int(rank)

def play_blackjack(userInfo):
    clearConsole()

    if userInfo["coin"] <= 0:
        print("\n[!] 보유 코인이 부족합니다.")
        input("\n엔터를 누르면 돌아갑니다.")
        return
    
    print("┌───────────────────────────────────┐")
    print("  카드 배틀 테이블에 입장하셨습니다.")
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
    dealer_card = deck.pop()
    user_card = deck.pop()

    clearConsole()

    print("┌───────────────────────────────────┐")
    print(f"  DEALER  ▶  [{dealer_card}]")
    print(f"  PLAYER  ▶  [{user_card}]")
    print("└───────────────────────────────────┘")

    dealer = calculate_score(dealer_card)
    player = calculate_score(user_card)

    if player > dealer:
        print(f" [ 승리 ] +{bet:,} 🪙")
        userInfo["coin"] += bet
    elif player < dealer:
        print(f" [ 패배 ] -{bet:,} 🪙")
        userInfo["coin"] -= bet
    else:
        print(" [ 무승부 ]")

    saveUserInfo(userInfo)
    print(f" [ 잔액 ] {userInfo['coin']:,} 🪙")
    input("\n엔터를 누르면 메인으로 돌아갑니다.")
