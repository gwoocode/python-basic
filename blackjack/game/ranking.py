from src.utils import clearConsole
from src.database import loadUser

def showMyStats(userInfo):
    clearConsole()

    total_game = (
        userInfo["win"]
        + userInfo["loss"]
        + userInfo["draw"]
    )

    if total_game > 0:
        win_rate = (userInfo["win"] / total_game) * 100
    else:
        win_rate = 0

    bar_length = 20
    filled_length = round(bar_length * win_rate / 100)
    gauge_bar = "#" * filled_length + "." * (bar_length - filled_length)

    print("┌───────────────────────────────────┐")
    print(f"         USER ID  │ {userInfo['name']}")
    print(f"         MY COIN  │ {userInfo['coin']:,}")
    print("└───────────────────────────────────┘")

    print(f"         TOTAL    │ {total_game} ")


    print("   ───────────────────────────────")

    print(f"         WINS     │ {userInfo['win']} 회")
    print(f"         DRAWS    │ {userInfo['draw']} 회")
    print(f"         LOSSES   │ {userInfo['loss']} 회")

    print(f"\n         WIN RATE │ {win_rate:.2f}%")
    print(f"       [{gauge_bar}]")
    print("   ───────────────────────────────")
    input("엔터를 누르면 돌아갑니다.")
    


def showRanking():
    clearConsole()

    print(" ⚑ Top 5 랭킹")
    userList = loadUser()
    sortedList = sorted(userList, key=lambda x: x["coin"], reverse=True)
    
    print("┌───────────────────────────────────┐")
    print("  순위    아이디        코인")
    print("└───────────────────────────────────┘")
    
    for i in range(1, 6):
        if i <= len(sortedList):
            user = sortedList[i - 1]
            name = user['name'].upper()
            coin = f"{user['coin']:,}"
            print(f"  [{i}]     {name:<14}{coin}")
        else:
            print(f"  [{i}]     {'-':<14}-")
            
    print("└───────────────────────────────────┘")
    input("엔터를 누르면 돌아갑니다.")