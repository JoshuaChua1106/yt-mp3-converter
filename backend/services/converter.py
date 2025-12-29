import yt_dlp
import os
import sys

def get_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS  # Path when running as .exe
    except Exception:
        base_path = os.path.abspath(".")  # Path when running as .py
    return os.path.join(base_path, relative_path)

def run_converter(youtube_url, output_folder="downloads"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Get the absolute path to the ffmpeg binary using PyInstaller-compatible method
    ffmpeg_bin_path = get_resource_path("bin")
    ffmpeg_path = os.path.join(ffmpeg_bin_path, 'ffmpeg.exe')

    # Configuration ofor yt_dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        # If part of a playlist, put it in a subfolder. If not, just the downloads folder.
        'outtmpl': {
            'default': f'{output_folder}/%(title)s.%(ext)s',
            'playlist': f'{output_folder}/%(playlist_title)s/%(title)s.%(ext)s'
        },
        
        # This is the "Magic" part that triggers the conversion
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        
        # WSL specific: ensures it finds FFmpeg
        'noplaylist': False,        # Allow playlists
        'extract_flat': False,      # Ensure it actually downloads the audio, not just metadata
        'playlist_items': '1-20',   # SAFETY: Limit to first 20 songs so your PC doesn't explode

        'prefer_ffmpeg': True,
        'keepvideo': False,  # Deletes the original video/m4a after mp3 is made
        'ffmpeg_location': ffmpeg_path,  # Use local ffmpeg binary
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"[*] Processing: {youtube_url}")
            ydl.download([youtube_url])
        return True
    except Exception as e:
        print(f"[!] Error: {e}")
        return False