"""read config.yml"""
import logging
import os
import yaml

from pathlib import Path
from dotenv import load_dotenv


logger = logging.getLogger(__name__)

load_dotenv()


def env(key: str, default: any = None) -> any:
    return os.environ.get(key, default)


def config(key: str) -> any:
    if _config.get(key):
        return _config.get(key)
    return None


# DEBUG
DEBUG = False

debug = env("DEBUG")
if debug and isinstance(debug, str) or isinstance(debug, bool):
    DEBUG = bool(eval(debug))

# APP_DIR
APP_DIR = Path(__file__).resolve().parent.parent.parent
if env("APP_DIR", None):
    APP_DIR = Path(env("APP_DIR"))

# AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
# AWS_DEFAULT_REGION = env("AWS_DEFAULT_REGION")
# AWS_BUCKET_ID = env("AWS_BUCKET_ID")

# CONF_DIR
CONF_DIR = APP_DIR / 'config'
if env("CONF_DIR"):
    CONF_DIR = Path(env("CONF_DIR"))

if not os.path.isdir(CONF_DIR):
    logger.warning(f"{CONF_DIR} does not exist")

# read config.yml
_config = {}
_conf = CONF_DIR / 'config.yml'

if os.path.isfile(_conf):
    with open(_conf, 'r', encoding="utf-8") as config_yaml:
        _config = yaml.safe_load(config_yaml)

# STATIC_DIR
STATIC_DIR = APP_DIR / "static"
if env("STATIC_DIR"):
    STATIC_DIR = Path(env("STATIC_DIR"))

