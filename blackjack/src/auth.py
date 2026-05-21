import re
from src.utils import hash_password, clearConsole
from src.database import loadUser, saveUser

def createUser(userName, userPass):
    userList = loadUser()
    hashed_pass = hash_password(userPass)

    newUser = {
        "name": userName.lower(),
        "hashed_pass": hashed_pass,
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
    
    createUser(name, pw)
    
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
