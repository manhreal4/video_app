import csv

def save_library_to_csv(library):
    with open('videos.csv', 'w', newline='') as f: # Open CSV
        csvwriter = csv.writer(f) # Create object
        csvwriter.writerow(['ID', 'Name', 'Director', 'Rating', 'Plays']) # Write 1 row to CSV
        # Loop through each item
        for video_id, video_info in library.items():
            csvwriter.writerow([video_id, video_info.name, video_info.director, video_info.rating, video_info.play_count]) # Write a row to CSV for each video
