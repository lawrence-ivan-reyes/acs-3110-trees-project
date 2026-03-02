#!python3

from avl_tree import AVLTree


class OrderedTreeMap:
    """an ordered map that keeps key-value pairs sorted by key
    unlike a hash map, supports range queries and ordered traversal"""

    def __init__(self, items=None):
        """initialize map w/ optional iterable of (key, value) tuples"""
        self._tree = AVLTree(items)

    def put(self, key, value):
        """insert or update a key-value pair
        TODO: running time: O(log n) — delegates to avl insert"""
        self._tree.insert(key, value)

    def get(self, key, default=None):
        """return value for key, or default if not found
        TODO: running time: O(log n) — delegates to avl search"""
        result = self._tree.search(key)
        if result is None:
            return default
        return result

    def remove(self, key):
        """remove a key, raises KeyError if not found
        TODO: running time: O(log n) — delegates to avl delete"""
        self._tree.delete(key)

    def keys(self):
        """return all keys in sorted order"""
        return [k for k, v in self._tree.items_in_order()]

    def values(self):
        """return all values in key-sorted order"""
        return [v for k, v in self._tree.items_in_order()]

    def items(self):
        """return all (key, value) pairs in sorted key order"""
        return self._tree.items_in_order()

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        result = self._tree.search(key)
        if result is None:
            raise KeyError(key)
        return result

    def __delitem__(self, key):
        self.remove(key)

    def __contains__(self, key):
        return self._tree.contains(key)

    def __len__(self):
        return len(self._tree)

    def __iter__(self):
        """iterate over keys in sorted order"""
        for key, value in self._tree.items_in_order():
            yield key

    def __repr__(self):
        """return string representation of this map"""
        items = ', '.join(f'{k!r}: {v!r}' for k, v in self._tree.items_in_order())
        return f'OrderedTreeMap({{{items}}})'


def main():
    movie_map = OrderedTreeMap()

    movie_map['Parasite'] = 8.5
    movie_map['Whiplash'] = 8.5
    movie_map['Prisoners'] = 8.2
    movie_map['The Prestige'] = 8.5
    movie_map['Oddity'] = 6.7

    print(f'Map size: {len(movie_map)}')
    print(f'Whiplash rating: {movie_map["Whiplash"]}')
    print(f'Contains "Parasite": {"Parasite" in movie_map}')

    print('\nAll movies (sorted by title):')
    for key in movie_map:
        print(f'  {key}: {movie_map[key]}')

    del movie_map['Oddity']
    print(f'\nAfter deleting "Oddity": {len(movie_map)} movies')


if __name__ == '__main__':
    main()
