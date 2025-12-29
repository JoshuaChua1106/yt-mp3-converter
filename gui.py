import customtkinter as ctk
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog
import sys
import os
import threading
from backend.services.converter import run_converter


# Set the appearance and color theme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window configuration
        self.title("YouTube to MP3 Converter")
        self.geometry("600x400")

        # Grid layout configuration
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        
        # Initialize output folder variable
        self.output_folder = "downloads"

        # 1. Title Label
        self.label = ctk.CTkLabel(self, text="YouTube MP3 Downloader", font=ctk.CTkFont(size=24, weight="bold"))
        self.label.grid(row=0, column=0, padx=20, pady=20)

        # 2. URL Entry Field
        self.url_entry = ctk.CTkEntry(self, placeholder_text="Paste YouTube URL here...", width=450)
        self.url_entry.grid(row=1, column=0, padx=20, pady=10)

        # 3. Output Folder Frame (contains entry and browse button)
        self.folder_frame = ctk.CTkFrame(self)
        self.folder_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        self.folder_frame.grid_columnconfigure(0, weight=1)
        
        # Output folder entry
        self.folder_entry = ctk.CTkEntry(self.folder_frame, placeholder_text="Output folder...", width=350)
        self.folder_entry.insert(0, self.output_folder)
        self.folder_entry.configure(state="readonly")
        self.folder_entry.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="ew")
        
        # Browse button
        self.browse_button = ctk.CTkButton(self.folder_frame, text="Browse", command=self.browse_folder, width=80)
        self.browse_button.grid(row=0, column=1, padx=(5, 10), pady=10)

        # 4. Download Button
        self.download_button = ctk.CTkButton(self, text="Download MP3", command=self.download_event)
        self.download_button.grid(row=3, column=0, padx=20, pady=20)

        # 5. Progress Label (Optional feedback)
        self.status_label = ctk.CTkLabel(self, text="", text_color="gray")
        self.status_label.grid(row=4, column=0, pady=10)

    def browse_folder(self):
        folder = filedialog.askdirectory(title="Select Output Folder")
        if folder:
            self.output_folder = folder
            self.folder_entry.configure(state="normal")
            self.folder_entry.delete(0, "end")
            self.folder_entry.insert(0, folder)
            self.folder_entry.configure(state="readonly")

    def download_event(self):
        url = self.url_entry.get()
        
        if not url:
            messagebox.showwarning("Error", "Please paste a URL first!")
            return

        # Start the download
        self.status_label.configure(text=f"Downloading", text_color="yellow")
        self.download_button.configure(state="disabled")
        
        thread = threading.Thread(target=self.download_thread, args=(url,), daemon=True)
        thread.start()

    def download_thread(self, url):
        try:
            print(f"User wants to download: {url}")
            print(f"Output folder: {self.output_folder}")
            
            # Call converter with selected output folder
            success = run_converter(url, self.output_folder)

            if success:
                # Only show success if run_converter actually returned True
                self.after(0, lambda: self.status_label.configure(text="Success!", text_color="green"))
                self.after(0, lambda: messagebox.showinfo("Done", "MP3 Downloaded successfully!"))
            else:
                # Handle the case where the downloader caught its own error and returned False
                self.after(0, lambda: self.status_label.configure(text="Download Failed", text_color="red"))
                self.after(0, lambda: messagebox.showerror("Error", "The conversion failed. Check your URL or internet."))

        except Exception as e:
            self.after(0, lambda: messagebox.showerror("Error", f"Failed: {str(e)}"))
            self.after(0, lambda: self.status_label.configure(text="Error", text_color="red"))
        
        finally:
            # Always re-enable the button
            self.after(0, lambda: self.download_button.configure(state="normal"))

if __name__ == "__main__":
    app = App()
    app.mainloop()