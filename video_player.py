import tkinter as tk
from tkinter import messagebox as msb

from video_library import load_library_from_csv
from file_manager import save_library_to_csv

import font_manager as fonts

from check_videos import CheckVideos
from create_video_list import CreateVideoList



# Press the "Check Videos" button
def check_videos_clicked():
    status_lbl.configure(text="Check Videos button was clicked!") # Update status
    load_library_from_csv()  # Update data from CSV file
    CheckVideos(tk.Toplevel(window)) # Create child window

# Press the "Create Video List" button
def create_videos_clicked():
    status_lbl.configure(text="Create Video List button was clicked!") # Update status
    load_library_from_csv()  # Update data from CSV file
    CreateVideoList(tk.Toplevel(window)) # Create child window
    
# Initialize the main window
window = tk.Tk()
window.geometry("400x150+20+20") # Update Size and Position
window.title("Video Player") # Set title
window.tk_setPalette(background="#FBEAEB", foreground="#2F3C7E") # Set background color and text color

# Font configuration
fonts.configure()

# Create title labels
header_lbl = tk.Label(window, text="Select an option\nby clicking one\nof the buttons below")
header_lbl.grid(row=0, column=0, rowspan=2, sticky='W')
     
# "Check Videos" button
check_videos_btn = tk.Button(window, text="Check Videos",foreground="#FBEAEB", background="#2F3C7E", command=check_videos_clicked)
check_videos_btn.grid(row=0, column=1, padx=10, pady=10, sticky='W')
# "Create Video List" button
create_video_list_btn = tk.Button(window, text="Create Video List",foreground="#FBEAEB", background="#2F3C7E", command=create_videos_clicked)
create_video_list_btn.grid(row=1, column=1, padx=10, pady=10)

# Create status labels
status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
status_lbl.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the main loop of the application to display the window
window.mainloop()
