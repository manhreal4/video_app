import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import messagebox as msb

import csv

import video_library as lib

from video_library import library
from video_library import load_library_from_csv
from file_manager import save_library_to_csv
from library_item import LibraryItem

import font_manager as fonts


# Function that sets the content for a text area in the user interface
def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class CheckVideos():
    
    # Constructor for the class
    def __init__(self, window):
        window.geometry("850x350+20+400") # Update Size and Position
        window.title("Check Videos") # Set title
        window.tk_setPalette(background="#FBEAEB", foreground="#2F3C7E") # Set background color and text color
        self.video_lib = VideoLib()  # Initialize a video_lib object

        # "List All Videos" button
        list_videos_btn = tk.Button(window, text="List All Videos",foreground="#FBEAEB", background="#2F3C7E", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        # Video ID data input area
        enter_lbl = tk.Label(window, text="Enter Video ID", background="#FBEAEB")
        enter_lbl.grid(row=0, column=2, padx=10, pady=10, sticky='E')
    
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=3, padx=10, pady=10)

        # "Check Video" button
        check_video_btn = tk.Button(window, text="Check Video",foreground="#FBEAEB", background="#2F3C7E", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=4)

        # Video list display area
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1,rowspan=5, column=0, columnspan=3, sticky="W", padx=10, pady=10)       
        self.list_txt.configure(background="#F0A07C", foreground="#4A274F")

        # Details
        tk.Label(window, text="ID :", width=7).grid(row=1, column=3, sticky="W")
        tk.Label(window, text="Name :", width=7).grid(row=2, column=3, sticky="W")
        tk.Label(window, text="Director :", width=7).grid(row=3, column=3, sticky="W")
        tk.Label(window, text="Rating :", width=7).grid(row=4, column=3, sticky="W")
        tk.Label(window, text="Plays :", width=7).grid(row=5, column=3, sticky="W")

        # Create entries to display detailed information of the video
        # ID
        self.id_entry = tk.Entry(window, width=24)
        self.id_entry.grid(row=1, column=4,columnspan=2, sticky="W", padx=2, pady=2)
        # Name
        self.name_entry = tk.Entry(window, width=24)
        self.name_entry.grid(row=2, column=4,columnspan=2, sticky="W", padx=2, pady=2)
        # Director
        self.director_entry = tk.Entry(window, width=24)
        self.director_entry.grid(row=3, column=4,columnspan=2, sticky="W", padx=2, pady=2)
        # Rating
        self.rating_entry = tk.Entry(window, width=24)
        self.rating_entry.grid(row=4, column=4,columnspan=2, sticky="W", padx=2, pady=2)
        # Plays
        self.plays_label = tk.Label(window, text="", width=10)
        self.plays_label.grid(row=5, column=4,columnspan=2, sticky="W", padx=2, pady=2)

        # Function buttons
        # "Add" button
        self.btn_add = tk.Button(window, text='Add',foreground="#FBEAEB", background="#2F3C7E", command=self.add_video)
        self.btn_add.grid(row=6, column=3, sticky='W')
        # "Update" button
        self.btn_update = tk.Button(window, text='Update',foreground="#295F2D", background="#FFE67C", command=self.update_video)
        self.btn_update.grid(row=6, column=4, sticky='W')
        # "Delete" button
        self.btn_delete = tk.Button(window, text='Delete',foreground="#FCE77D", background="#F96167", command=self.delete_video)
        self.btn_delete.grid(row=6, column=5, sticky='W')
        
        # Create status labels
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10), background="#FBEAEB", foreground="#2F3C7E")
        self.status_lbl.grid(row=6, column=0, columnspan=4, sticky="W", padx=10, pady=10)
        
        self.list_videos_clicked()
        
    # Press the "Check Video" button
    def check_video_clicked(self):
        self.status_lbl.configure(text="Check Video button was clicked!") # Update status

        key = self.input_txt.get() # Lấy id từ ô nhập liệu input_txt

        # Kiểm tra xem ID có tồn tại hay không
        if not self.video_lib.is_id_exists(key):
            msb.showwarning('Warning', f'Video with ID {key} does not exist!')
            return

        name = lib.get_name(key) # Lấy tên video có id là key
        director = lib.get_director(key) # Lấy tên tác giả
        rating = lib.get_rating(key) # Lấy xếp hạng
        play_count = lib.get_play_count(key) # Lấy lượt phát

        # Cập nhật giá trị của các entry để hiển thị thông tin chi tiết
        # ID
        self.id_entry.delete(0, tk.END)
        self.id_entry.insert(0, key)
        # Name
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, name)
        # Director
        self.director_entry.delete(0, tk.END)
        self.director_entry.insert(0, director)
        # Rating
        self.rating_entry.delete(0, tk.END)
        self.rating_entry.insert(0, rating)
        # Plays
        self.plays_label.configure(text=play_count)
            
    # Press the "List All Videos" button
    def list_videos_clicked(self):
        self.status_lbl.configure(text="List Videos button was clicked!") # Update status
        self.video_lib.load_videos_from_csv()  # Load lại danh sách video từ CSV
        video_list = lib.list_all() # Lấy tất cả các video
        set_text(self.list_txt, video_list) # Cập nhật văn bản lên vùng cuộn list_txt

    # Press the "Delete" button
    def delete_video(self):
        self.status_lbl.configure(text="Delete button was clicked!") # Update status
        id = self.input_txt.get() # Get id from input_txt input box
        if not id: # If id has not been entered
            msb.showwarning('Warning', 'Please enter the ID of the video to be deleted!')
            return
        # Check if ID exists in the library
        if not self.video_lib.is_id_exists(id):
            msb.showwarning('Warning', f'Video with ID {id} does not exist!')
            return
        # Confirm before deleting
        confirmation = msb.askyesno('Confirmation', f"Are you sure you want to delete the video with ID {id}?")
        if confirmation:
            try:
                self.video_lib.delete_video_by_id(id) # Delete videos from video library
                self.list_txt.delete(1.0, tk.END) # Delete videos from the displayed list
                self.list_videos_clicked() # Reload video list
                msb.showinfo('Success', 'The video has been successfully deleted!')
            except Exception as e:
                msb.showerror('Error', e)

    # Press the "Update" button
    def update_video(self):
        self.status_lbl.configure(text="Update button was clicked!") # Update status
        id = self.input_txt.get() # Get ID from input area
        if not id: # If id has not been entered
            msb.showwarning('Warning', 'Please enter the ID of the video to be updated!')
            return
        # Check if ID exists in the library
        if not self.video_lib.is_id_exists(id):
            msb.showwarning('Warning', f'Video with ID {id} does not exist!')
            return
        # Confirm before updating
        confirmation = msb.askyesno('Confirmation', f"Are you sure you want to update the video with ID {id}?")
        if confirmation:
            try:
                # Get video information from input boxes
                name = self.name_entry.get()
                director = self.director_entry.get()
                rating = self.rating_entry.get() 
                # Update videos in video library
                self.video_lib.update_video_by_id(id, name, director, int(rating))
                # Delete and reload video list
                self.list_videos_clicked()
                self.video_lib.save_videos_to_csv()
                msb.showinfo('Success', 'The video has been updated successfully!')
            except Exception as e:
                msb.showerror('Error', e)

    # Press the "Add" button
    def add_video(self):
        self.status_lbl.configure(text="Add button was clicked!") # Update status
        # Get video information from input boxes
        id = self.id_entry.get()
        name = self.name_entry.get()
        director = self.director_entry.get()
        rating = self.rating_entry.get()
        # Check if ID exists in the library
        if self.video_lib.is_id_exists(id):
            msb.showwarning('Warning', f'Video with ID {id} already exists!')
            return
        # Confirm before adding
        confirmation = msb.askyesno('Confirmation', f"Are you sure you want to add a new video?")
        if confirmation:
            try:
                video = Video(id, name, director, int(rating)) # Create a video object
                self.video_lib.add_video(video) # Add videos to video library
                self.list_txt.insert(tk.END, name) # Add videos to the display list
                library[id] = LibraryItem(name, director, int(rating)) # Update the library
                self.video_lib.save_videos_to_csv() # Save video to CSV file
                msb.showinfo('Success', 'The video has been added successfully!')
            except Exception as e:
                msb.showerror('Error', e)

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    CheckVideos(window)     # open the CheckVideo GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc

# Class defines a video
class Video:
    def __init__(self, id, name, director, rating):
        self.__id = id
        self.__name = name
        self.__director = director
        self.__rating = rating
        
    @property 
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('name cannot be empty')
        self.__name = value
        
    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, value):
        if value == '':
            raise ValueError('director cannot be empty')
        self.__director = value
        
    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if value < 0 and value > 5:
            raise ValueError('rating cannot be negative')
        self.__rating = value
        
        
        
# Video library management class
class VideoLib:
    
    def __init__(self):
        self.__videos = []
        self.load_videos_from_csv()  # Load videos from CSV file

    # Method to check if ID already exists or not
    def is_id_exists(self, id):
        return id in library

    # Method to load video list from CSV file
    def load_videos_from_csv(self):
        self.__videos.clear()  # Delete existing videos
        library.clear()  # Delete existing library
        with open('videos.csv', 'r') as f:
            csvreader = csv.reader(f)
            header = next(csvreader)  # Ignore headers
            play_index = header.index('Plays')
            for row in csvreader:
                id = row[0]
                name = row[1]
                director = row[2]
                rating = int(row[3])
                plays = int(row[play_index])
                video = Video(id, name, director, rating)
                self.__videos.append(video)
                # Update library here
                library[id] = LibraryItem(name, director, rating, plays)

    # Method to get names of all videos
    def get_name(self):
        return [video.name for video in self.__videos]

    # Method to get information of a specific video
    def get_video(self, i):
        video = self.__videos[i]
        return video.id, video.name, video.director, video.rating
        
    # Video update method
    def update_video_by_id(self, id, name, director, rating):
        # Find videos based on id, assign idex = index of that video in the list, if not found return None
        index = next((i for i, video in enumerate(self.__videos) if video.id == id), None)
        if index is not None: # Check video exists or not
            video = self.__videos[index] # Assign the found video to the video variable
            # Assign new information
            video.name = name
            video.director = director
            video.rating = rating
            self.save_videos_to_csv()  # Save video to CSV file after update
        else:
            raise ValueError(f'Video with ID {id} not found')

    # Method to add video
    def add_video(self, v):
        self.__videos.append(v)
        self.save_videos_to_csv()  # Save videos to CSV file after adding
        
    # Method to delete video
    def delete_video_by_id(self, id):
        # Find videos based on id, assign idex = index of that video in the list, if not found return None
        index = next((i for i, video in enumerate(self.__videos) if video.id == id), None) 
        if index is not None: # Check video exists or not
            del self.__videos[index] # Remove videos from the list
            del library[id]  # Delete videos from gallery
            self.save_videos_to_csv()  # Save changes to CSV file after deletion
        else:
            raise ValueError(f'Video with ID {id} not found!')

    # Method to save information to CSV file
    def save_videos_to_csv(self):
        # Open the csv file, if it exists, it will be overwritten, if not, a new one will be created
        with open('videos.csv', 'w', newline='') as f:
            csvwriter = csv.writer(f) # Create an object to write data to the opened CSV file
            csvwriter.writerow(['ID', 'Name', 'Director', 'Rating', 'Plays'])  # Write a header row
            # Browse the list of videos
            for video in self.__videos:
                # Write 1 row of data, default view is 0
                csvwriter.writerow([video.id, video.name, video.director, video.rating, 0]) 
                
    
