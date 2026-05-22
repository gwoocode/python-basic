import sys
import os
import time
from src.auth import signup, login, resetPassword
from src.utils import clearConsole
from src.database import loadUser
from game.blackjack import play_blackjack

def main():
    current_user = None
    
    while True:
        clearConsole()
        
        if current_user is None:
            print("┌───────────────────────────────────┐")
            print("  메인 메뉴")
            print("└───────────────────────────────────┘")
            print("  [1] 로그인")
            print("  [2] 회원가입")
            print("  [3] 비밀번호 찾기")
            print("  [4] 프로그램 종료")
            print("─────────────────────────────────────")
            
            choice = input(" 선택 > ")
            if choice == "1":
                current_user = login()
            elif choice == "2":
                signup()
            elif choice == "3":
                resetPassword()
            elif choice == "4":
                print("\n 프로그램을 종료합니다.")
                time.sleep(1)
                clearConsole()
                sys.exit()

        else:
            print("┌───────────────────────────────────┐")
            print(f"  ID   > {current_user['name'].upper()}")
            print(f"  COIN > {current_user['coin']:,}")
            print("└───────────────────────────────────┘")
            print("  [1] 게임하기")
            print("  [2] 로그아웃")
            print("  [3] 프로그램 종료")
            print("─────────────────────────────────────")
            
            game_choice = input(" 선택 > ")
            if game_choice == "1":
                play_blackjack(current_user)

                userList = loadUser()
                for u in userList:
                    if u["name"] == current_user["name"]:
                        current_user = u
                        break

            if game_choice == "2":
                print("\n 로그아웃되었습니다.")
                current_user = None
                time.sleep(1)

            elif game_choice == "3":
                print("\n 프로그램을 종료합니다.")
                time.sleep(1)
                clearConsole()
                sys.exit()
if __name__ == "__main__":
    main()