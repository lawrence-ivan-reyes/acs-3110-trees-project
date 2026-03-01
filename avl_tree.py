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
