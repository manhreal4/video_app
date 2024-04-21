import pytest
from library_item import LibraryItem

# Test for info function
def test_library_item_info():
    # Create a LibraryItem object
    item = LibraryItem("The Shawshank Redemption", "Frank Darabont", 5)
    # Check the return result of the info function
    assert item.info() == "The Shawshank Redemption - Frank Darabont *****"

# Test for stars function
def test_library_item_stars():
    # Create a LibraryItem object
    item = LibraryItem("Inception", "Christopher Nolan", 4)
    # Check the return result of the stars function
    assert item.stars() == "****"

# Test update_play_count function with positive count value
def test_library_item_update_play_count_positive():
    # Create a LibraryItem object
    item = LibraryItem("Interstellar", "Christopher Nolan", 5)
    # Update the number of plays with a count of 3
    item.update_play_count(3)
    # Check if the play count has been updated correctly
    assert item.play_count == 3


# Test update_play_count function with negative count value
def test_library_item_update_play_count_negative():
    # Create a LibraryItem object
    item = LibraryItem("The Godfather", "Francis Ford Coppola", 5)
    # Update the number of plays with a count of -2
    item.update_play_count(-2)
    # Check if the play count has been updated correctly
    assert item.play_count == -2  # Play count has been updated to -2
