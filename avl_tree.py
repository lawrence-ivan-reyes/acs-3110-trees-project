#!python3

class AVLNode:
    """a single node in the avl tree storing a key-value pair"""

    def __init__(self, key, value=None):
        """initialize node with given key and optional value"""
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def __repr__(self):
        """return a string representation of this node"""
        return f'AVLNode({self.key!r})'

class AVLTree:
    """avl tree supporting insert, search & in-order traversal
    keys must be comparable, duplicate keys update stored value!!"""

    def __init__(self, items=None):
        """initialize avl tree and insert given items if any
        items: iterable of (key, value) tuples"""
        self.root = None
        self.size = 0
        if items is not None:
            for key, value in items:
                self.insert(key, value)

    def is_empty(self):
        """check if tree is empty
        TODO: running time: O(1) — just checking a counter"""
        return self.size == 0

    def insert(self, key, value=None):
        """insert key-value pair, update value if key already exists
        TODO: running time: O(log n) — tree is balanced (after rotations added)
        TODO: memory usage: O(log n) — recursive call stack depth"""
        self.root = self._insert(self.root, key, value)

    def search(self, key):
        """return value for given key, or None if not found
        TODO: running time: O(log n) — balanced tree height
        TODO: memory usage: O(log n) — recursive call stack"""
        node = self._search(self.root, key)
        if node is None:
            return None
        return node.value

    def contains(self, key):
        """check if given key exists in tree
        TODO: running time: O(log n) — delegates to search"""
        return self._search(self.root, key) is not None

    def items_in_order(self):
        """return list of all (key, value) pairs in ascending key order
        TODO: running time: O(n) — visits every node
        TODO: memory usage: O(n) — stores all pairs in list"""
        items = []
        self._traverse_in_order(self.root, items)
        return items

    def _height(self, node):
        """return height of node, or 0 if None"""
        if node is None:
            return 0
        return node.height

    def _update_height(self, node):
        """recalculate and set height of given node"""
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _insert(self, node, key, value):
        """recursively insert key-value pair into subtree rooted at node
        return new root of subtree after insertion"""
        if node is None:
            self.size += 1
            return AVLNode(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            # key already exists, update value
            node.value = value
            return node

        self._update_height(node)
        return node

    def _search(self, node, key):
        """recursively search for key in subtree rooted at node
        return node if found, None otherwise"""
        if node is None:
            return None
        if key < node.key:
            return self._search(node.left, key)
        elif key > node.key:
            return self._search(node.right, key)
        else:
            return node

    def _traverse_in_order(self, node, items):
        """traverse subtree in-order, appending (key, value) pairs to items list"""
        if node is not None:
            self._traverse_in_order(node.left, items)
            items.append((node.key, node.value))
            self._traverse_in_order(node.right, items)

    def __repr__(self):
        """return string representation of this avl tree"""
        return f'AVLTree({self.size} nodes)'

    def __len__(self):
        return self.size

    def __contains__(self, key):
        return self.contains(key)
