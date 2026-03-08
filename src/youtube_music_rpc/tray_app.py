from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pystray
from PIL import Image, ImageDraw

PROJECT_ROOT = Path(__file__).resolve().parents[2]
MAIN_SCRIPT = PROJECT_ROOT / "src" / "youtube_music_rpc" / "main.py"


def create_icon() -> Image.Image:
    image = Image.new("RGB", (64, 64), "white")
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((8, 8, 56, 56), radius=12, fill=(255, 0, 0))
    draw.polygon([(26, 20), (26, 44), (46, 32)], fill="white")
    return image


class TrayController:
    def __init__(self) -> None:
        self.process: subprocess.Popen | None = None

    def start_service(self, icon: pystray.Icon | None = None, item=None) -> None:
        if self.process and self.process.poll() is None:
            return
        self.process = subprocess.Popen([sys.executable, str(MAIN_SCRIPT)], cwd=str(PROJECT_ROOT))

    def stop_service(self, icon: pystray.Icon | None = None, item=None) -> None:
        if self.process and self.process.poll() is None:
            self.process.terminate()
            self.process.wait(timeout=5)
        self.process = None

    def quit_app(self, icon: pystray.Icon, item=None) -> None:
        self.stop_service()
        icon.stop()


def run_tray() -> None:
    controller = TrayController()
    controller.start_service()
    icon = pystray.Icon(
        "YouTubeMusicDiscordRPC",
        create_icon(),
        "YouTube Music Discord RPC",
        menu=pystray.Menu(
            pystray.MenuItem("Start Service", controller.start_service),
            pystray.MenuItem("Stop Service", controller.stop_service),
            pystray.MenuItem("Quit", controller.quit_app),
        ),
    )
    icon.run()


if __name__ == "__main__":
    run_tray()
