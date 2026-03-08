# YouTube Music Discord Rich Presence

A polished Windows project that shows the song currently playing on **YouTube Music** in **Discord Rich Presence**, with album art, playback progress, startup support, optional system tray mode, and executable build support.

---

## Features

- Detects the currently playing track from Windows media sessions
- Updates Discord Rich Presence in near real time
- Shows title, artist, album, and playback progress
- Tries to fetch album art automatically
- Supports silent startup on Windows boot
- Includes an optional tray application
- Includes PyInstaller build script for `.exe` packaging
- Includes multilingual installation guides

---

## Project Structure

```text
youtube-music-discord-rpc/
├─ src/
│  └─ youtube_music_rpc/
│     ├─ __init__.py
│     ├─ config.py
│     ├─ logging_utils.py
│     ├─ main.py
│     ├─ rpc.py
│     └─ tray_app.py
├─ scripts/
│  └─ run_hidden.vbs
├─ docs/
│  ├─ INSTALL.de.md
│  ├─ INSTALL.en.md
│  ├─ INSTALL.es.md
│  └─ INSTALL.tr.md
├─ .gitignore
├─ build_exe.bat
├─ config.example.json
├─ LICENSE
├─ README.md
├─ requirements.txt
└─ setup_startup.py
```

---

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/monstercantaliadam/youtube-music-discord-rpc.git
cd youtube-music-discord-rpc
```

### 2. Create a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Copy configuration

```bash
copy config.example.json config.json
```

### 5. Run the app

```bash
python src\youtube_music_rpc\main.py
```

---

## Discord Setup

You can use the default Client ID already included in `config.example.json`, or create your own application:

1. Open the Discord Developer Portal.
2. Create a new application.
3. Copy your **Client ID**.
4. Put it into `config.json`.
5. Optionally upload your own Rich Presence assets.

Recommended asset keys:

- `youtube_music`
- your own custom artwork names if you want stricter branding control

---

## Windows Startup

To make the project launch silently when Windows starts:

```bash
python setup_startup.py
```

This creates a shortcut in the Windows Startup folder that runs the VBS launcher.

---

## Tray Application

To launch the optional tray version:

```bash
python src\youtube_music_rpc\tray_app.py
```

This starts the service and adds a small tray icon so you can start, stop, or quit it without a terminal window glaring at you like an angry robot.

---

## Build EXE

To build a standalone Windows executable:

```bat
build_exe.bat
```

Generated output will be placed in the `dist/` folder.

---

## Configuration

Example `config.json`:

```json
{
  "client_id": "1474703271959465994",
  "poll_interval_seconds": 15,
  "supported_apps": ["youtube", "chrome", "msedge", "opera", "firefox"],
  "buttons": {
    "enabled": true,
    "label": "Listen on YouTube Music"
  },
  "logging": {
    "level": "INFO"
  }
}
```

---

## Notes

- This project is intended for **Windows** because it uses Windows media session APIs.
- Discord must be running for Rich Presence updates to work.
- Some media sessions depend on the browser and tab state, because software likes to be dramatic.

---

## Documentation

Multilingual installation guides are available here:

- [English](docs/INSTALL.en.md)
- [Türkçe](docs/INSTALL.tr.md)
- [Deutsch](docs/INSTALL.de.md)
- [Español](docs/INSTALL.es.md)

---

## License

This project is released under the **MIT License**.
