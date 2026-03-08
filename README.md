# 🎵 YouTube Music Discord Rich Presence

<p align="center">
  <img src="https://i.imgur.com/9vfpwa1.png" width="700">
</p>

<p align="center">
Show the song currently playing on <b>YouTube Music</b> directly in your <b>Discord Rich Presence</b>.
</p>

<p align="center">

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

</p>

---

## ✨ Overview

**YouTube Music Discord Rich Presence** is a Windows application that detects the song currently playing on **YouTube Music** and shows it in **Discord Rich Presence**.

It automatically updates your Discord status with:

- Song title
- Artist
- Album artwork
- Playback progress

The application is lightweight and designed to run quietly in the background.

---

## 🚀 Features

- Detects the currently playing track from Windows media sessions  
- Updates Discord Rich Presence in near real time  
- Displays song title, artist, album and playback progress  
- Attempts to automatically fetch album artwork  
- Supports silent startup on Windows boot  
- Optional system tray application  
- Includes PyInstaller build script for `.exe` packaging  
- Multilingual installation guides included  

---

## 📁 Project Structure

```
youtube-music-discord-rpc/
├─ src/
│  └─ youtube_music_rpc/
│     ├─ __init__.py
│     ├─ config.py
│     ├─ logging_utils.py
│     ├─ main.py
│     ├─ rpc.py
│     └─ tray_app.py
│
├─ scripts/
│  └─ run_hidden.vbs
│
├─ docs/
│  ├─ INSTALL.de.md
│  ├─ INSTALL.en.md
│  ├─ INSTALL.es.md
│  └─ INSTALL.tr.md
│
├─ .gitignore
├─ build_exe.bat
├─ config.example.json
├─ LICENSE
├─ README.md
├─ requirements.txt
└─ setup_startup.py
```

---

# ⚡ Quick Start

## 1. Clone the repository

```
git clone https://github.com/monstercantaliadam/youtube-music-discord-rpc.git
cd youtube-music-discord-rpc
```

---

## 2. Create a virtual environment

```
python -m venv .venv
.venv\Scripts\activate
```

---

## 3. Install dependencies

```
pip install -r requirements.txt
```

---

## 4. Create configuration file

```
copy config.example.json config.json
```

---

## 5. Run the application

```
python src\youtube_music_rpc\main.py
```

When a song plays on YouTube Music, your **Discord Rich Presence** will update automatically.

---

# 🎮 Discord Setup

You can use the default Client ID already included in `config.example.json`, or create your own Discord application.

Steps:

1. Open the **Discord Developer Portal**
2. Create a new application
3. Copy the **Client ID**
4. Put it into `config.json`
5. Optionally upload custom Rich Presence assets

Recommended asset key:

```
youtube_music
```

---

# 🖥 Windows Startup

To make the application launch automatically when Windows starts:

```
python setup_startup.py
```

This creates a shortcut in the **Windows Startup folder** that runs the application silently.

---

# 📌 Tray Application

To launch the optional tray version:

```
python src\youtube_music_rpc\tray_app.py
```

This adds a small tray icon that allows you to start, stop or exit the service without keeping a terminal window open.

---

# 📦 Build EXE

To build a standalone Windows executable:

```
build_exe.bat
```

The compiled executable will appear in the:

```
dist/
```

folder.

---

# ⚙ Configuration

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

# 📚 Documentation

Installation guides are available in multiple languages:

- English → `docs/INSTALL.en.md`
- Türkçe → `docs/INSTALL.tr.md`
- Deutsch → `docs/INSTALL.de.md`
- Español → `docs/INSTALL.es.md`

---

# ⚠ Notes

- This project is designed specifically for **Windows** because it uses Windows Media Session APIs.
- Discord must be running for Rich Presence updates to appear.
- Media detection depends on the browser and tab state.

---

# 📜 License

This project is released under the **MIT License**.
