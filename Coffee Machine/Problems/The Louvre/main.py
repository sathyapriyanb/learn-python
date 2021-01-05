class Painting:
    museum = 'Louvre'

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def print_name(self):
        print(f'"{self.title}" by {self.artist} ({self.year}) hangs in the {Painting.museum}.')


p1 = Painting(input(), input(), input())
p1.print_name()