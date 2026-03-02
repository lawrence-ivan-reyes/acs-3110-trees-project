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
