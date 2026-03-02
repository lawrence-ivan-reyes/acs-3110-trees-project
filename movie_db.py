#!python3

import csv
from tree_map import OrderedTreeMap

class MovieDatabase:
    """a movie database that stores movies in an ordered tree map
    supports search, browse, filter by rating range, and filter by genre"""

    def __init__(self):
        """initialize empty movie database w/ two tree maps
        one sorted by title, one sorted by rating"""
        self.by_title = OrderedTreeMap()
        self.by_rating = OrderedTreeMap()

    def load_from_csv(self, filepath):
        """load movies from a csv file"""
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                title = row['title']
                rating = float(row['rating'])
                year = int(row['year'])
                genre = row['genre']
                movie = {'title': title, 'rating': rating, 'year': year, 'genre': genre}
                self.by_title[title] = movie
                # use (rating, title) as key so movies w/ same rating are sorted by title
                self.by_rating[(rating, title)] = movie

    def search(self, title):
        """search for a movie by exact title"""
        return self.by_title.get(title)

    @property
    def size(self):
        return len(self.by_title)
