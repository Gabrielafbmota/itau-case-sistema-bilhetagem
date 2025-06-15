from dotenv import load_dotenv
import os

load_dotenv()


def get_env_var(key):
    try:
        return os.environ[key]
    except KeyError:
        print(f"Environment variable {key} not found")
        raise
