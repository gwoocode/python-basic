import re
from src.utils import hash_password, clearConsole
from src.database import loadUser, saveUser

def createUser(userName, userPass):
    userList = loadUser()
    hashed_pass = hash_password(userPass)

    newUser = {
        "name": userName.lower(),
        "hashed_pass": hashed_pass
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

