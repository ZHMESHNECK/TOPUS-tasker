from datetime import datetime, timedelta, timezone
from TASKER.core.config import secret_jwt, algorithm
from TASKER.db.models import UserDB
from fastapi import Cookie
import hashlib
import jwt


def hash_password(password: str) -> str:
    """Hash a password using SHA-256 algorithm."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def generate_token(user: UserDB) -> str:
    exp = datetime.now(timezone.utc) + timedelta(days=7)
    payload = {
        "exp": exp,
        "id": user.id,
        "username": user.username,
        "role": user.role
    }
    return jwt.encode(payload, secret_jwt, algorithm=algorithm)


def decode_token(TOPUS: str = Cookie(default=None)):
    try:
        payload = jwt.decode(TOPUS, secret_jwt, algorithms=algorithm)
        return payload
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False


def chat_id_generator(user_id1: int, user_id2: int):
    if user_id1 > user_id2:
        user_id1, user_id2 = user_id2, user_id1

    id = f'{str(user_id1)}/{str(user_id2)}'
    return hashlib.sha1(id.encode('utf-8')).hexdigest()
