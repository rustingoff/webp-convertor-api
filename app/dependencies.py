import jwt
from .config import config


def parse_token(token: str) -> bool:
    conf = config.get_config()
    try:
        jwt.decode(token, conf['secret_key'], algorithms=[conf['secret_alg']])
        return True
    except Exception as e:
        print(e)
        return False
