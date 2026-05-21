import sys
import os
from src.auth import signup
from src.utils import clearConsole

def main():
    while True:
        clearConsole()

        print("┌───────────────────────────────────┐")
        print("  메인 메뉴")
        print("└───────────────────────────────────┘")
        print("  [1] 로그인")
        print("  [2] 회원가입")
        print("  [3] 프로그램 종료")
        print("─────────────────────────────────────")
        
        choice = input(" 선택 > ")
        if choice == "1":
            input(" 로그인 선택\n 엔터를 누르면 돌아갑니다.")
        elif choice == "2":
            signup()
        elif choice == "3":
            sys.exit()

if __name__ == "__main__":
    main()