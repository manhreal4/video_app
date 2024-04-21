from library_item import LibraryItem
import csv
from file_manager import save_library_to_csv


# Initialize a dictionary to store library items
library = {}

# Add items to the library
library["01"] = LibraryItem("Tom and Jerry", "Fred Quimby", 4, 0)
library["02"] = LibraryItem("Breakfast at Tiffany's", "Blake Edwards", 5, 0)
library["03"] = LibraryItem("Casablanca", "Michael Curtiz", 2, 0)
library["04"] = LibraryItem("The Sound of Music", "Robert Wise", 1, 0)
library["05"] = LibraryItem("Gone with the Wind", "Victor Fleming", 3, 0)

# The function reads data from the CSV file and updates the library
def load_library_from_csv():
    with open('videos.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the first row
        for row in reader:
            id, name, director, rating, plays = row 
            library[id] = LibraryItem(name, director, int(rating), int(plays))

# List all items in the library
def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output

# Get the name of an item based on its code
def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None

# Get the director name of an item based on the code number
def get_director(key):
    try:
        item = library[key]
        return item.director
    except KeyError:
        return None

# Get the rating of an item based on its code
def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1

# Set rating for an item based on code number
def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return

# Get the number of plays of an item based on the code
def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1

# Increase the number of plays of an item by 1 based on the code
def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return