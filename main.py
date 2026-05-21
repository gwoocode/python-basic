import sys
import os

def clearConsole():
    os.system(
        "cls" if os.name in ("nt", "dos") else "clear"
    )

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
            input(" 회원가입 선택\n 엔터를 누르면 돌아갑니다.")
        elif choice == "3":
            sys.exit()

if __name__ == "__main__":
    main()