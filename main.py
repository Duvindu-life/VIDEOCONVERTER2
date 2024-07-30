import subprocess
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def convert_video(input_path):
    if not os.path.isfile(input_path):
        messagebox.showerror("Error", f"File not found: {input_path}")
        return

    ffmpeg_path = r"C:\ffmpeg\ffmpeg-2024-07-28-git-e7d3ff8dcd-full_build\ffmpeg-2024-07-28-git-e7d3ff8dcd-full_build\bin\ffmpeg.exe"

    if not os.path.isfile(ffmpeg_path):
        messagebox.showerror("Error", f"FFmpeg executable not found: {ffmpeg_path}")
        return

    base, ext = os.path.splitext(input_path)
    output_path = f"{base}_converted.mp4"

    command = [
        ffmpeg_path,
        '-i', input_path,
        '-c:v', 'libx264',
        '-c:a', 'aac',
        '-strict', 'experimental',
        output_path
    ]

    try:
        subprocess.run(command, check=True)
        messagebox.showinfo("Success", f"Successfully converted {input_path} to {output_path}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error during conversion: {e}")
    except FileNotFoundError as e:
        messagebox.showerror("Error", f"File not found error: {e}")

def select_file():
    input_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")])
    if input_path:
        convert_video(input_path)

def create_gui():
    root = tk.Tk()
    root.title("Video Converter")

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    label = tk.Label(frame, text="Select a video file to convert:")
    label.pack(pady=5)

    convert_button = tk.Button(frame, text="Select File", command=select_file)
    convert_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
change