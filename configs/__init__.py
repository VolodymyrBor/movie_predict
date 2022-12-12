from pathlib import Path

import yaml

from .models import Config

CONFIG_DIR = Path(__file__).parent
CONFIG_FILE = CONFIG_DIR / 'config.yaml'

ROOT_DIR = CONFIG_DIR.parent


def load_config() -> Config:
    raw_config = yaml.safe_load(CONFIG_FILE.read_text())
    return Config.parse_obj(raw_config)


CONFIG = load_config()
