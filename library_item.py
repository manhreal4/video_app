class LibraryItem:
    def __init__(self, name, director, rating=0, play_count=0):
        self.name = name
        self.director = director
        self.rating = rating
        self.play_count = play_count

    def info(self):
        return f"{self.name} - {self.director} {self.stars()}"

    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars

    # Update the number of plays
    def update_play_count(self, count):
        self.play_count += count