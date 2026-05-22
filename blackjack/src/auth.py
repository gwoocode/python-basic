import re
from src.utils import hash_password, clearConsole, SECURITY_QUESTIONS
from src.database import loadUser, saveUser

def createUser(userName, userPass, questionIdx, securityHint):
    userList = loadUser()
    hashed_pass = hash_password(userPass)
    hashed_hint = hash_password(securityHint.strip().lower())

    newUser = {
        "name": userName.lower(),
        "hashed_pass": hashed_pass,
        "security_question_idx": questionIdx,
        "security_hint": hashed_hint,
        "coin": 1000,
        "locked": False,
        "fail_count": 0
    }
    
    userList.append(newUser)
    saveUser(userList)
    return newUser

def signup():
    while True:
        clearConsole()
        print("┌───────────────────────────────────┐")
        print("  회원 가입")
        print("└───────────────────────────────────┘")
        
        name = input("  이름 > ")
        
        if not re.match(r"^[a-zA-Z0-9]+$", name):
            print("\n [!] 영문자 또는 숫자만 사용 가능합니다.")
            input(" 엔터를 누르면 다시 시도합니다.")
            continue
            
        userList = loadUser()
        if any(user["name"] == name.lower() for user in userList):
            print("\n [!] 이미 존재하는 이름입니다.")
            input(" 엔터를 누르면 다시 시도합니다.")
            continue
        
        break
        
    pw = input("  비밀번호 > ")
    
    while True:
        clearConsole()
        print("┌───────────────────────────────────┐")
        print("  회원가입 (보안 질문)")
        print("└───────────────────────────────────┘")
        for i, q in enumerate(SECURITY_QUESTIONS, 1):
            print(f"  [{i}] {q}")
        print("─────────────────────────────────────")
        
        try:
            choice_input = input(" 선택 > ")
            q_choice = int(choice_input) - 1
            
            if 0 <= q_choice < len(SECURITY_QUESTIONS):
                break
            else:
                print(f"\n [!] 1부터 {len(SECURITY_QUESTIONS)} 사이의 숫자만 입력해주세요.")
                input(" 엔터를 누르면 다시 시도합니다...")
        except ValueError:
            print("\n [!] 올바른 숫자를 입력해주세요.")
            input(" 엔터를 누르면 다시 시도합니다...")
            
    hint = input(" 답변 > ")
    
    createUser(name, pw, q_choice, hint)
    
    clearConsole()
    print("┌───────────────────────────────────┐")
    print(f"  회원가입이 완료되었습니다!")
    print("  [가입 보너스] 1,000 Coin 지급")
    print("└───────────────────────────────────┘\n")
    input(" 메인 메뉴로 이동하려면 엔터를 누르세요.")

def login():
    clearConsole()
    userList = loadUser()
    
    print("┌───────────────────────────────────┐")
    print("  로그인")
    print("└───────────────────────────────────┘")
    userName = input("  이름 > ")
    userPass = input("  비밀번호 > ")
    hashed = hash_password(userPass)

    for user in userList:
        if user["name"] == userName.lower():
            if user.get("locked", False):
                print("\n [잠금] 계정이 잠겨 있습니다. 비밀번호 찾기를 이용해주세요.")
                input(" 엔터를 누르면 메뉴로 돌아갑니다.")
                return None

            if user["hashed_pass"] == hashed:
                user["fail_count"] = 0
                saveUser(userList)
                return user
            else:
                user["fail_count"] = user.get("fail_count", 0) + 1
                if user["fail_count"] >= 5:
                    user["locked"] = True
                    print("\n [경고] 비밀번호 5회 오류로 인해 계정이 잠겼습니다.")
                else:
                    print(f"\n [!] 비밀번호가 일치하지 않습니다. ({user['fail_count']}/5)")
                
                saveUser(userList)
                input(" 엔터를 누르면 메뉴로 돌아갑니다.")
                return None

    print("\n [!] 존재하지 않는 이름입니다.")
    input(" 엔터를 누르면 메뉴로 돌아갑니다.")
    return None

def resetPassword():
    clearConsole()
    userList = loadUser()

    print("┌───────────────────────────────────┐")
    print("  비밀번호 찾기")
    print("└───────────────────────────────────┘")
    userName = input("  이름 > ")

    for user in userList:
        if user["name"] == userName.lower():
            q_idx = user.get("security_question_idx", 0)
            print(f"\n  질문 > {SECURITY_QUESTIONS[q_idx]}")
            
            hint_input = input("  답변 > ")
            hashed_hint_input = hash_password(hint_input.lower())
            
            if user["security_hint"] == hashed_hint_input:
                new_pw = input("  새 비밀번호 > ")
                
                user["hashed_pass"] = hash_password(new_pw)
                user["locked"] = False
                user["fail_count"] = 0
                saveUser(userList)
                
                print("\n  비밀번호 변경 및 잠금 해제가 완료.")
                input("  엔터를 누르면 메뉴로 돌아갑니다.")
                return
            else:
                print("\n [!] 보안 답변이 일치하지 않습니다.")
                input(" 엔터를 누르면 메뉴로 돌아갑니다.")
                return
                
    print("\n [!] 해당 사용자를 찾을 수 없습니다.")
    input(" 엔터를 누르면 메뉴로 돌아갑니다.")