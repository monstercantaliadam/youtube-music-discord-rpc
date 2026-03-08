# Installationsanleitung (Deutsch)

## Anforderungen

- Windows 10 oder neuer
- Python 3.10+
- Discord-Desktop-App
- YouTube Music in einem unterstützten Browser

## Installationsschritte

### 1. Projekt klonen oder herunterladen

```bash
git clone https://github.com/monstercantaliadam/youtube-music-discord-rpc.git
cd youtube-music-discord-rpc
```

### 2. Virtuelle Umgebung erstellen

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

### 4. Konfigurationsdatei erstellen

```bash
copy config.example.json config.json
```

### 5. Anwendung starten

```bash
python src\youtube_music_rpc\main.py
```

## Optional: Mit Windows starten

```bash
python setup_startup.py
```

## Optional: Mit Tray-Symbol starten

```bash
python src\youtube_music_rpc\tray_app.py
```

## Optional: EXE erstellen

```bat
build_exe.bat
```
