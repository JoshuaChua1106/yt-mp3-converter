import customtkinter as ctk
import tkinter.messagebox as messagebox
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from backend.services.converter import run_converter


# Set the appearance and color theme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window configuration
        self.title("YouTube to MP3 Converter")
        self.geometry("600x350")

        # Grid layout configuration (2 rows, 1 column)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # 1. Title Label
        self.label = ctk.CTkLabel(self, text="YouTube MP3 Downloader", font=ctk.CTkFont(size=24, weight="bold"))
        self.label.grid(row=0, column=0, padx=20, pady=20)

        # 2. URL Entry Field
        self.url_entry = ctk.CTkEntry(self, placeholder_text="Paste YouTube URL here...", width=450)
        self.url_entry.grid(row=1, column=0, padx=20, pady=10)

        # 3. Download Button
        self.download_button = ctk.CTkButton(self, text="Download MP3", command=self.download_event)
        self.download_button.grid(row=2, column=0, padx=20, pady=20)

        # 4. Progress Label (Optional feedback)
        self.status_label = ctk.CTkLabel(self, text="", text_color="gray")
        self.status_label.grid(row=3, column=0, pady=10)

    def download_event(self):
        url = self.url_entry.get()
        
        if not url:
            messagebox.showwarning("Error", "Please paste a URL first!")
            return

        # For now, we just simulate the start
        self.status_label.configure(text=f"Connecting to YouTube...", text_color="yellow")
        self.download_button.configure(state="disabled")
        
        print(f"User wants to download: {url}")
        
        # This is where we will call your yt-dlp function later!
        success = run_converter(url)

        if success:
            print("MP3 Downloaded")
        else:
            print("Failed")

        # Reset UI
        self.download_button.configure(state="normal")
        self.status_label.configure(text="Ready", text_color="green")

if __name__ == "__main__":
    app = App()
    app.mainloop()