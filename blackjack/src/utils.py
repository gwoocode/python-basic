import os
import hashlib

SECURITY_QUESTIONS = (
    "가장 기억에 남는 여행지는?",
    "내 보물 1호는?",
    "가장 좋아하는 어릴 적 별명은?",
    "어릴 적 꿈은?",
    "존경하는 인물의 이름은?"
)

def clearConsole():
    os.system(
        "cls" if os.name in ("nt", "dos")
        else "clear"
    )

def hash_password(password):
    return hashlib.sha256(
        password.encode()
    ).hexdigest()