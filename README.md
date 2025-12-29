# YouTube to MP3 Converter

A simple YouTube to MP3 converter with both GUI and command-line interfaces.

## Setup

### 1. Download FFmpeg

1. Download FFmpeg from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Extract the downloaded files
3. Copy `ffmpeg.exe`, `ffplay.exe`, and `ffprobe.exe` to the `bin/` folder in this project
4. Your `bin/` folder should contain:
   ```
   bin/
   ├── ffmpeg.exe
   ├── ffplay.exe
   └── ffprobe.exe
   ```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface

Run the main script with a YouTube URL:

```bash
python backend/main.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

Optional: Specify output folder:
```bash
python backend/main.py "https://www.youtube.com/watch?v=VIDEO_ID" --output "my_downloads"
```

### Graphical User Interface

Run the GUI application:

```bash
python gui.py
```

1. Paste a YouTube URL in the input field
2. Click "Browse" to select an output folder (optional)
3. Click "Download MP3" to start the conversion

## Building Executable

### Build with PyInstaller

```bash
pyinstaller gui.spec
```

This creates a single executable file at `dist/yt-converter.exe`

### Running the Executable

1. Navigate to the `dist/` folder
2. Double-click `yt-converter.exe` or run from command line:
   ```bash
   ./dist/yt-converter.exe
   ```

## Features

- Download individual videos or playlists (limited to first 20 songs)
- Choose output folder through GUI
- High-quality MP3 conversion (192kbps)
- Cross-platform support
- Self-contained executable for easy distribution

## Notes

- Downloads are saved to a `downloads/` folder by default
- Playlist downloads are organized in subfolders
- The application requires an internet connection to download videos