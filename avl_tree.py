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

    def __repr__(self):
        """return string representation of this avl tree"""
        return f'AVLTree({self.size} nodes)'

    def __len__(self):
        return self.size
