import os
import hashlib

def clearConsole():
    os.system(
        "cls" if os.name in ("nt", "dos")
        else "clear"
    )

def hash_password(password):
    return hashlib.sha256(
        password.encode()
    ).hexdigest()