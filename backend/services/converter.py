import yt_dlp
import os

def run_converter(youtube_url, output_folder="downloads"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Configuration ofor yt_dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        # Naming: This saves it as 'Title.mp3' inside the downloads folder
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
        
        # This is the "Magic" part that triggers the conversion
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        
        # WSL specific: ensures it finds FFmpeg
        'prefer_ffmpeg': True,
        'keepvideo': False,  # Deletes the original video/m4a after mp3 is made
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"[*] Processing: {youtube_url}")
            ydl.download([youtube_url])
        return True
    except Exception as e:
        print(f"[!] Error: {e}")
        return False