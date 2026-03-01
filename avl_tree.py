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
        TODO: running time: O(log n) — balanced tree height
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

    def delete(self, key):
        """delete key from tree, raises KeyError if not found
        TODO: running time: O(log n) — balanced tree height
        TODO: memory usage: O(log n) — recursive call stack"""
        self.root = self._delete(self.root, key)
        self.size -= 1

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

    def _balance_factor(self, node):
        """return balance factor of node (left height - right height)
        avl invariant: must be -1, 0, or 1"""
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _rotate_right(self, z):
        """right rotation around z, used when left-heavy"""
        y = z.left
        t3 = y.right
        # perform rotation
        y.right = z
        z.left = t3
        # update heights (z first since its now lower)
        self._update_height(z)
        self._update_height(y)
        return y

    def _rotate_left(self, z):
        """left rotation around z, used when right-heavy"""
        y = z.right
        t2 = y.left
        # perform rotation
        y.left = z
        z.right = t2
        # update heights (z first since its now lower)
        self._update_height(z)
        self._update_height(y)
        return y

    def _rebalance(self, node):
        """check balance factor and apply rotations if needed
        handles all 4 cases: left-left, left-right, right-right, right-left"""
        self._update_height(node)
        bf = self._balance_factor(node)

        # left-heavy
        if bf > 1:
            # left-right case: rotate left child left first
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # right-heavy
        if bf < -1:
            # right-left case: rotate right child right first
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

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

        return self._rebalance(node)

    def _min_node(self, node):
        """return the node with the smallest key in subtree"""
        while node.left is not None:
            node = node.left
        return node

    def _delete(self, node, key):
        """recursively delete key from subtree rooted at node
        return new root of subtree after deletion"""
        if node is None:
            raise KeyError(key)

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # found the node to delete
            # case 1: no left child
            if node.left is None:
                return node.right
            # case 2: no right child
            if node.right is None:
                return node.left
            # case 3: two children — replace with in-order successor
            successor = self._min_node(node.right)
            node.key = successor.key
            node.value = successor.value
            node.right = self._delete(node.right, successor.key)

        return self._rebalance(node)

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

def main():
    tree = AVLTree()

    print('Inserting movies...')
    tree.insert('Parasite', 8.5)
    tree.insert('Whiplash', 8.5)
    tree.insert('Prisoners', 8.2)
    tree.insert('The Prestige', 8.5)
    tree.insert('Oddity', 6.7)

    print(f'Tree size: {tree.size}')
    print(f'Is empty: {tree.is_empty()}')

    # search for a movie
    rating = tree.search('Whiplash')
    print(f'Whiplash rating: {rating}')

    # check if movie exists
    print(f'Contains "Prisoners": {tree.contains("Prisoners")}')
    print(f'Contains "Avatar": {tree.contains("Avatar")}')

    # list all movies in alpha order
    print('\nAll movies (sorted by title):')
    for title, rating in tree.items_in_order():
        print(f'  {title}: {rating}')

    # delete a movie
    print('\nDeleting "Oddity"...')
    tree.delete('Oddity')
    print(f'Tree size: {tree.size}')
    print(f'Contains "Oddity": {tree.contains("Oddity")}')

    print('\nAll movies after deletion:')
    for title, rating in tree.items_in_order():
        print(f'  {title}: {rating}')


if __name__ == '__main__':
    main()
