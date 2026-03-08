# Installation Guide (English)

## Requirements

- Windows 10 or newer
- Python 3.10+
- Discord desktop application
- YouTube Music running in a supported browser

## Setup Steps

### 1. Clone or download the project

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

### 4. Create your configuration file

```bash
copy config.example.json config.json
```

### 5. Run the program

```bash
python src\youtube_music_rpc\main.py
```

## Optional: Start with Windows

```bash
python setup_startup.py
```

## Optional: Run with tray icon

```bash
python src\youtube_music_rpc\tray_app.py
```

## Optional: Build EXE

```bat
build_exe.bat
```
