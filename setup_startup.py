from __future__ import annotations

import os
from pathlib import Path

import winshell
from win32com.client import Dispatch

PROJECT_ROOT = Path(__file__).resolve().parent
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
VBS_PATH = SCRIPTS_DIR / "run_hidden.vbs"


def create_startup_shortcut() -> Path:
    startup_path = Path(winshell.startup())
    shortcut_path = startup_path / "YouTube Music Discord RPC.lnk"

    shell = Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(str(shortcut_path))
    shortcut.TargetPath = "wscript.exe"
    shortcut.Arguments = f'"{VBS_PATH}"'
    shortcut.WorkingDirectory = str(PROJECT_ROOT)
    shortcut.IconLocation = "wscript.exe,0"
    shortcut.Description = "Launch YouTube Music Discord RPC silently at Windows startup"
    shortcut.save()
    return shortcut_path


if __name__ == "__main__":
    output = create_startup_shortcut()
    print(f"Startup shortcut created: {output}")
