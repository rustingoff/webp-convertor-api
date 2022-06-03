import os

from dotenv import load_dotenv
from pathlib import Path


dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)


def get_config() -> dict:
    token_secret = os.getenv('TOKEN_SECRET_KEY')
    token_algorithm = os.getenv('TOKEN_ALGORITHM')

    config = {
        'secret_key': token_secret,
        'secret_alg': token_algorithm
    }

    return config
