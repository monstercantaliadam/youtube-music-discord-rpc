# Kurulum Rehberi (Türkçe)

## Gereksinimler

- Windows 10 veya üzeri
- Python 3.10+
- Discord masaüstü uygulaması
- Desteklenen bir tarayıcıda açık YouTube Music

## Kurulum Adımları

### 1. Projeyi klonlayın veya indirin

```bash
git clone https://github.com/monstercantaliadam/youtube-music-discord-rpc.git
cd youtube-music-discord-rpc
```

### 2. Sanal ortam oluşturun

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Bağımlılıkları kurun

```bash
pip install -r requirements.txt
```

### 4. Yapılandırma dosyasını oluşturun

```bash
copy config.example.json config.json
```

### 5. Uygulamayı çalıştırın

```bash
python src\youtube_music_rpc\main.py
```

## İsteğe Bağlı: Windows açılışında başlatma

```bash
python setup_startup.py
```

## İsteğe Bağlı: Tepsi simgesi ile çalıştırma

```bash
python src\youtube_music_rpc\tray_app.py
```

## İsteğe Bağlı: EXE oluşturma

```bat
build_exe.bat
```
