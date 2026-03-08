from __future__ import annotations

import asyncio
import sys

from youtube_music_rpc.config import load_config
from youtube_music_rpc.logging_utils import configure_logging
from youtube_music_rpc.rpc import YouTubeMusicRPC


def main() -> None:
    config = load_config()
    configure_logging(config.get("logging", {}).get("level", "INFO"))

    app = YouTubeMusicRPC(
        client_id=config["client_id"],
        supported_apps=config["supported_apps"],
        poll_interval=config["poll_interval_seconds"],
        button_label=config.get("buttons", {}).get("label", "Listen on YouTube Music"),
        buttons_enabled=bool(config.get("buttons", {}).get("enabled", True)),
    )

    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

    try:
        asyncio.run(app.run())
    except KeyboardInterrupt:
        print("Stopping YouTube Music Discord RPC...")


if __name__ == "__main__":
    main()
