import json

def loadUser():
    try:
        with open("users.txt", "r") as f:
            data = f.read()
            return json.loads(data) if data else []
    except FileNotFoundError:
        return []

def saveUser(userList):
    with open("users.txt", "w") as f:
        f.write(json.dumps(userList))

def saveUserInfo(userInfo):
    userList = loadUser()
    for i, user in enumerate(userList):
        if user["name"] == userInfo["name"]:
            userList[i] = userInfo
            break
    saveUser(userList)