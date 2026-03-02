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

    def all_by_title(self):
        """return all movies sorted alphabetically by title"""
        return self.by_title.values()

    def all_by_rating(self):
        """return all movies sorted by rating (ascending)"""
        return self.by_rating.values()

    def filter_by_genre(self, genre):
        """return all movies matching a genre, sorted by title"""
        results = []
        for title, movie in self.by_title.items():
            if movie['genre'].lower() == genre.lower():
                results.append(movie)
        return results

    def top_rated(self, n=10):
        """return top n movies by rating"""
        all_movies = list(self.by_rating.items())
        # reverse since by_rating is ascending!!
        all_movies.reverse()
        return [movie for _, movie in all_movies[:n]]

    @property
    def size(self):
        return len(self.by_title)

def main():
    """interactive cli for the movie database"""
    db = MovieDatabase()
    db.load_from_csv('movies.csv')
    print(f'Loaded {db.size} movies from movies.csv\n')

    while True:
        print('--- Movie Database ---')
        print('1. Search by title')
        print('2. Browse all (alphabetical)')
        print('3. Browse all (by rating)')
        print('4. Filter by genre')
        print('5. Top rated')
        print('6. Quit')

        choice = input('\nChoice: ').strip()

        if choice == '1':
            title = input('Enter movie title: ').strip()
            movie = db.search(title)
            if movie:
                print(f'\n  {movie["title"]} ({movie["year"]})')
                print(f'  Rating: {movie["rating"]} | Genre: {movie["genre"]}\n')
            else:
                print(f'\n  "{title}" not found\n')

        elif choice == '2':
            print('\nAll movies (A-Z):')
            for movie in db.all_by_title():
                print(f'  {movie["title"]} ({movie["year"]}) — {movie["rating"]}')
            print()

        elif choice == '3':
            print('\nAll movies (by rating):')
            for movie in db.all_by_rating():
                print(f'  {movie["rating"]} — {movie["title"]} ({movie["year"]})')
            print()

        elif choice == '4':
            genre = input('Enter genre: ').strip()
            movies = db.filter_by_genre(genre)
            if movies:
                print(f'\n{genre} movies:')
                for movie in movies:
                    print(f'  {movie["title"]} ({movie["year"]}) — {movie["rating"]}')
            else:
                print(f'\n  No movies found for genre "{genre}"')
            print()

        elif choice == '5':
            n = input('How many? (default 10): ').strip()
            n = int(n) if n else 10
            print(f'\nTop {n} rated movies:')
            for i, movie in enumerate(db.top_rated(n), 1):
                print(f'  {i}. {movie["title"]} ({movie["year"]}) — {movie["rating"]}')
            print()

        elif choice == '6':
            print('Goodbye!')
            break

        else:
            print('Invalid choice, try again\n')


if __name__ == '__main__':
    main()
