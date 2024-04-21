import tkinter as tk
from tkinter import messagebox as msb
from video_library import library
from video_library import load_library_from_csv
from file_manager import save_library_to_csv


class CreateVideoList:
    
    # Constructor for the class
    def __init__(self, window):
        # Assign the window object to the class's window property
        self.window = window 
        window.title("Create Video List") # Set title
        window.geometry("950x600+550+20") # Update Size and Position
        window.tk_setPalette(background="#FBEAEB", foreground="#2F3C7E") # Set background color and text color
        # Initialize an empty list
        self.selected_videos = []
        self.create_widgets() # Call the UI creation method
        load_library_from_csv()


    # Method to create user interface
    def create_widgets(self):
        # The section displays the videos in the library
        self.lbl_instruction = tk.Label(self.window, text="Create your own playlists")
        self.lbl_instruction.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        self.lbl_instruction = tk.Label(self.window, text="List all video")
        self.lbl_instruction.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.lst_videos = tk.Listbox(self.window, width=35, height=7, selectmode=tk.MULTIPLE)
        self.lst_videos.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.fill_videos()
        self.lst_videos.configure(background="#F0A07C", foreground="#4A274F")  # Set background color and text color
        
        # Display of the selected playlist
        self.lbl_instruction = tk.Label(self.window, text="Your playlist")
        self.lbl_instruction.grid(row=4, column=3, columnspan=2, padx=10, pady=10)
        
        self.lst_your_videos = tk.Listbox(self.window, width=35, height=7, selectmode=tk.MULTIPLE)
        self.lst_your_videos.grid(row=6,rowspan=3, column=3, columnspan=2, padx=10, pady=10)
        
        self.lst_your_videos.configure(background="#F0A07C", foreground="#4A274F") # Set background color and text color
        
        # "Add Video to Playlist" button
        self.btn_add_to_playlist = tk.Button(self.window, text="Add to Playlist",foreground="#FBEAEB", background="#2F3C7E", command=self.add_to_playlist)
        self.btn_add_to_playlist.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

        # "Run" button
        self.btn_run_playlist = tk.Button(self.window, text="Run",foreground="#FBEAEB", background="#2F3C7E", command=self.run_playlist)
        self.btn_run_playlist.grid(row=6, column=5, padx=10, pady=10)
        
        # "Remove" button
        self.btn_remove_playlist = tk.Button(self.window, text="Remove",foreground="#FCE77D", background="#F96167", command=self.remove_playlist)
        self.btn_remove_playlist.grid(row=7, column=5, padx=10, pady=10)
        
        # "Reset" button
        self.btn_reset_playlist = tk.Button(self.window, text="Reset",foreground="#295F2D", background="#FFE67C", command=self.reset_playlist)
        self.btn_reset_playlist.grid(row=8, column=5, padx=10, pady=10)
        
        # Status label
        self.status_lbl = tk.Label(self.window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=9, column=4, padx=10, pady=10)
        
        # Add dropdown menu for search option
        self.search_option = tk.StringVar()  # Variable to store search type
        self.search_option.set("Name")  # Default is to search by name

        self.option_menu = tk.OptionMenu(self.window, self.search_option, "Name", "Director", "ID")
        self.option_menu.grid(row=1, column=3, padx=0, pady=5)

        # Search input field
        self.entry_search_input = tk.Entry(self.window, width=30)
        self.entry_search_input.grid(row=1, column=4, padx=0, pady=5)
        
        # "Search" button
        self.btn_search = tk.Button(self.window, text="Search",foreground="#FBEAEB", background="#2F3C7E", command=self.search_videos)
        self.btn_search.grid(row=1, column=5, padx=5, pady=5)
        
        # Label displays search results
        self.lbl_instruction = tk.Label(self.window, text="Search videos")
        self.lbl_instruction.grid(row=0, column=3, columnspan=2, padx=10, pady=10)
        
        self.lbl_search_result = tk.Listbox(self.window, width=35, height=7, selectmode=tk.MULTIPLE)
        self.lbl_search_result.grid(row=3, column=3, columnspan=2, padx=10, pady=10)
        
        self.lbl_search_result.configure(background="#F0A07C", foreground="#4A274F")  # Set background color and text color
        
        # "Add" button
        self.btn_add_to_playlist_search = tk.Button(self.window, text="Add",foreground="#FBEAEB", background="#2F3C7E", command=self.add_selected_from_search)
        self.btn_add_to_playlist_search.grid(row=3, rowspan=3, column=5, padx=5, pady=5)
        
        # Label displays the video history that has just been played
        self.lbl_history_instruction = tk.Label(self.window, text="History")
        self.lbl_history_instruction.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
        
        self.lbl_play_history = tk.Listbox(self.window, width=35, height=4, selectmode=tk.MULTIPLE)
        self.lbl_play_history.grid(row=7,rowspan=2, column=0, columnspan=2, padx=10, pady=10)
        
        self.lbl_play_history.configure(background="#F0A07C", foreground="#4A274F")  # Set background color and text color
        
        # "Remove history" button
        self.btn_remove_history = tk.Button(self.window, text="Remove history",foreground="#FCE77D", background="#F96167", command=self.remove_history)
        self.btn_remove_history.grid(row=9, column=0, padx=5, pady=5)
        
        # "Remove all" button
        self.btn_remove_history_all = tk.Button(self.window, text="Remove all",foreground="#295F2D", background="#FFE67C", command=self.remove_history_all)
        self.btn_remove_history_all.grid(row=9, column=1, padx=5, pady=5)
        
        
    # Method to fill the UI's video data
    def fill_videos(self):
        # Delete all items already in the list
        self.lst_videos.delete(0, tk.END) 
        # Loop through each key - value pair in the library and add it to the display list
        for video_id, video_info in library.items():
            # Add a new item to the video list, displaying information about the video
            self.lst_videos.insert(tk.END, f"{video_id} : {video_info.name} - {video_info.director}")


    # Press the "Add to Playlist" button
    def add_to_playlist(self):
        self.status_lbl.configure(text="Add to Playlist button was clicked!") # Update status
        load_library_from_csv()
        # Get index of selected videos in display list
        selected_indices = self.lst_videos.curselection()
        if not selected_indices: # Check if no video is selected
            msb.showwarning("Warning", "Please select at least one video to add to playlist.")
            return
        # Loop through selected video indexes
        for idx in selected_indices:
            # Get the index of the video in the display list
            video_index = int(idx)
            # Get the ID of the video from the index
            video_id = list(library.keys())[video_index]
            # Check if the video already exists in the playlist
            if video_id not in self.selected_videos: # Not existed yet
                self.selected_videos.append(video_id) # Add to playlist
                self.lst_your_videos.insert(tk.END, f"{video_id} : {library[video_id].name} - {library[video_id].director}") # Displayed
            else: # Already exist
                msb.showinfo("Info", f"{library[video_id].name} - {library[video_id].director} is already in the playlist.")   
                

    # Press the "Run" button
    def run_playlist(self):
        self.status_lbl.configure(text="Run button was clicked!") # Update status
        load_library_from_csv()
        # Get index of selected videos in display list
        selected_indices = self.lst_your_videos.curselection()
        if not selected_indices: # Kiểm tra nếu không có video được chọn
            msb.showwarning("Warning", "Please select a video to play!")
            return
        # Initialize a list to save played videos
        played_videos = []
        # Loop through the indexes of selected videos in the user's playlist
        for idx in selected_indices:
            video_id = self.selected_videos[idx]  # Get video ID from selected video list based on index
            # Increase the number of plays of the video in the library by 1 time
            library[video_id].play_count += 1
            # Add video information to the play history list
            played_videos.append(f"{video_id} : {library[video_id].name} - {library[video_id].director}")
        save_library_to_csv(library)# Save changes to the library
        self.fill_videos() # Cập nhật lại danh sách video hiển thị
        # Show play history in lbl_play_history
        self.update_play_history(played_videos, append=True)  # Add to playback history
        msb.showinfo("Success", "Selected videos played!")

    
    # Press the "Remove" button
    def remove_playlist(self):
        self.status_lbl.configure(text="Remove button was clicked!") # Update status
        # Get index of selected videos in display list
        selected_indices = self.lst_your_videos.curselection()
        if not selected_indices: # Check if no video is selected
            msb.showwarning("Warning", "Please select at least one video to remove from the playlist.")
            return
        # Show warning before deletion
        confirmation = msb.askokcancel("Confirmation", "Are you sure you want to remove the selected items from the playlist?")
        if confirmation:
            # Loop through selected indexes in reverse order to ensure that removing items does not cause index errors.
            for idx in selected_indices[::-1]:
                # Remove videos from the displayed playlist
                self.lst_your_videos.delete(idx)
                # Get video ID from selected video list based on index
                video_id = self.selected_videos.pop(idx)  # Remove element at index idx from self.selected_videos
            save_library_to_csv(library) # Save changes to the library
            self.fill_videos() # Update the displayed video list
            msb.showinfo("Remove Playlist", "Videos removed from the playlist successfully.")



    # Press the "Reset" button
    def reset_playlist(self):
        self.status_lbl.configure(text="Reset button was clicked!") # Update status
        confirmation = msb.askokcancel("Confirmation", "Are you sure you want to reset the playlist?") # Show warning before resetting playlist
        if confirmation:
            self.lst_your_videos.delete(0, tk.END) # Reset playlist to empty
            self.selected_videos = []
            msb.showinfo("Playlist Reset", "Playlist reset successfully.")
        
    
    # Press the "Search" button
    def search_videos(self):
        self.status_lbl.configure(text="Search button was clicked!") # Update status
        self.lbl_search_result.delete(0, tk.END) # Delete previous search results in the displayed list
        # Get information about the search type and search keywords from the user
        search_option = self.search_option.get()
        search_input = self.entry_search_input.get().strip().lower()
        if not search_input: # If search information has not been entered
            msb.showwarning("Warning", "Please enter search keywords!")
            return
        # Initialize a list containing search results
        found_videos = []
        # Browse the library
        for video_id, video_info in library.items():
            if search_option == "Name":
                match_condition = search_input in video_info.name.lower() # Keywords contain a piece of information, regardless of capitalization or lowercase
            elif search_option == "Director":
                match_condition = search_input in video_info.director.lower() # Keywords contain a piece of information, regardless of capitalization or lowercase
            elif search_option == "ID":
                match_condition = search_input == video_id
            if match_condition: # Add to search list if results are available
                found_videos.append(f"{video_id} : {video_info.name} - {video_info.director}")
        # Display results
        if found_videos: # If there is search information
            for video in found_videos:
                self.lbl_search_result.insert(tk.END, video)
        else: # No search information available
            self.lbl_search_result.insert(tk.END, "No matching videos were found!")


    # Press the "Add" button
    def add_selected_from_search(self):
        self.status_lbl.configure(text="Add button was clicked!") # Update status
        load_library_from_csv()
        selected_videos = [self.lbl_search_result.get(idx) for idx in self.lbl_search_result.curselection()] # Identify the selected video
        if not selected_videos: # If not selected
            msb.showwarning("Warning", "Please select at least one video from the search list!")
            return
        # Check if the video already exists in the playlist
        for video in selected_videos:
            video_id = video.split(' : ')[0] # Get the ID of the video
            if video_id not in self.selected_videos: # If not
                self.selected_videos.append(video_id) # Add to video ID list
                self.lst_your_videos.insert(tk.END, video) # Show videos
            else: # If already exists
                msb.showinfo("Information", f"{video} already in the playlist!")

                
        
    # Method to update playback history
    def update_play_history(self, played_videos, append=True):
        load_library_from_csv()
        if not append: # If append = False
            self.lbl_play_history.delete(0, tk.END) # Delete all entries in play history
        # Loop through the list, displaying information for each video
        for video in played_videos:
            self.lbl_play_history.insert(tk.END, video)


    # Press the "Remove history" button
    def remove_history(self):
        self.status_lbl.configure(text="Remove history button was clicked!") # Update status
        # Get index of selected videos in display list
        selected_indices = self.lbl_play_history.curselection()
        if not selected_indices: # If the item to be deleted has not been selected
            msb.showwarning("Warning", "Please select at least one video from the play history!")
            return
        # Loop through the indices of selected items in the play history from last to first
        for idx in selected_indices[::-1]:
            self.lbl_play_history.delete(idx)


    # Press the "Remove all" button
    def remove_history_all(self):
        self.status_lbl.configure(text="Remove all button was clicked!") # Update status
        self.lbl_play_history.delete(0, tk.END) # Delete all entries from 0 to END

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Create Video List")
    app = CreateVideoList(window)
    window.mainloop()


