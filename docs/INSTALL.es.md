# Guía de Instalación (Español)

## Requisitos

- Windows 10 o superior
- Python 3.10+
- Aplicación de escritorio de Discord
- YouTube Music abierto en un navegador compatible

## Pasos de instalación

### 1. Clona o descarga el proyecto

```bash
git clone https://github.com/monstercantaliadam/youtube-music-discord-rpc.git
cd youtube-music-discord-rpc
```

### 2. Crea un entorno virtual

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Crea el archivo de configuración

```bash
copy config.example.json config.json
```

### 5. Ejecuta la aplicación

```bash
python src\youtube_music_rpc\main.py
```

## Opcional: Iniciar con Windows

```bash
python setup_startup.py
```

## Opcional: Ejecutar con icono en la bandeja

```bash
python src\youtube_music_rpc\tray_app.py
```

## Opcional: Crear EXE

```bat
build_exe.bat
```
