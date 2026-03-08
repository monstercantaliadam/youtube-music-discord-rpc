@echo off
setlocal
cd /d %~dp0

if not exist .venv (
    python -m venv .venv
)

call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt

pyinstaller ^
  --noconfirm ^
  --onefile ^
  --windowed ^
  --name YouTubeMusicDiscordRPC ^
  --paths src ^
  src\youtube_music_rpc\main.py

echo.
echo Build completed. Check the dist folder.
pause
