"""read config.yml"""

import os
import yaml

from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


def env(key: str, default: any = None) -> any:
    return os.environ.get(key, default)


DEBUG = False

debug = env("DEBUG")
if debug and isinstance(debug, str) or isinstance(debug, bool):
    DEBUG = bool(eval(debug))

APP_DIR = Path(__file__).resolve().parent.parent.parent
if env("APP_DIR", None):
    APP_DIR = Path(env("APP_DIR"))

# AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
# AWS_DEFAULT_REGION = env("AWS_DEFAULT_REGION")
# AWS_BUCKET_ID = env("AWS_BUCKET_ID")

with open(APP_DIR / 'config' / 'config.yml') as config_yaml:
    _config = yaml.safe_load(config_yaml)


def config(key: str) -> any:
    if _config.get(key):
        return _config.get(key)
    return None
