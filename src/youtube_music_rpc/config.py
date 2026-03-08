from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict

APP_NAME = "YouTube Music Discord RPC"
DEFAULT_CLIENT_ID = "1474703271959465994"
DEFAULT_POLL_INTERVAL = 15
DEFAULT_CONFIG: Dict[str, Any] = {
    "client_id": DEFAULT_CLIENT_ID,
    "poll_interval_seconds": DEFAULT_POLL_INTERVAL,
    "supported_apps": [
        "youtube",
        "chrome",
        "msedge",
        "opera",
        "firefox",
        "brave",
        "vivaldi",
        "yandex",
        "music",
    ],
    "buttons": {
        "enabled": True,
        "label": "Listen on YouTube Music"
    },
    "logging": {
        "level": "INFO"
    }
}


def get_project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def get_config_path() -> Path:
    env_path = os.getenv("YT_RPC_CONFIG")
    if env_path:
        return Path(env_path).expanduser().resolve()
    return get_project_root() / "config.json"


def load_config() -> Dict[str, Any]:
    config_path = get_config_path()
    if not config_path.exists():
        return DEFAULT_CONFIG.copy()

    with config_path.open("r", encoding="utf-8") as file:
        user_config = json.load(file)

    merged = DEFAULT_CONFIG.copy()
    for key, value in user_config.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            nested = merged[key].copy()
            nested.update(value)
            merged[key] = nested
        else:
            merged[key] = value
    return merged
