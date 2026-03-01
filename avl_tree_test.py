#!python3

import unittest
from avl_tree import AVLTree, AVLNode


class AVLTreeTest(unittest.TestCase):

    def test_init(self):
        tree = AVLTree()
        assert tree.size == 0
        assert tree.root is None
        assert tree.is_empty() is True

    def test_insert_one(self):
        tree = AVLTree()
        tree.insert('Parasite', 8.5)
        assert tree.size == 1
        assert tree.is_empty() is False
        assert tree.root.key == 'Parasite'
        assert tree.root.value == 8.5

    def test_insert_multiple(self):
        tree = AVLTree()
        tree.insert('Parasite', 8.5)
        tree.insert('Whiplash', 8.5)
        tree.insert('Prisoners', 8.2)
        assert tree.size == 3

    def test_insert_duplicate_updates_value(self):
        tree = AVLTree()
        tree.insert('Parasite', 8.0)
        tree.insert('Parasite', 8.5)
        # size should not increase
        assert tree.size == 1
        # value should be updated
        assert tree.search('Parasite') == 8.5

    def test_init_with_items(self):
        items = [('Parasite', 8.5), ('Whiplash', 8.5), ('Oddity', 6.7)]
        tree = AVLTree(items)
        assert tree.size == 3
        assert tree.contains('Parasite') is True
        assert tree.contains('Whiplash') is True
        assert tree.contains('Oddity') is True

    def test_search(self):
        tree = AVLTree()
        tree.insert('Parasite', 8.5)
        tree.insert('Whiplash', 8.5)
        # search existing key
        assert tree.search('Parasite') == 8.5
        assert tree.search('Whiplash') == 8.5
        # search non-existing key
        assert tree.search('Avatar') is None

    def test_contains(self):
        tree = AVLTree()
        tree.insert('Parasite', 8.5)
        assert tree.contains('Parasite') is True
        assert tree.contains('Avatar') is False
        # also test dunder method
        assert ('Parasite' in tree) is True
        assert ('Avatar' in tree) is False

    def test_delete(self):
        tree = AVLTree()
        tree.insert('Parasite', 8.5)
        tree.insert('Whiplash', 8.5)
        tree.insert('Prisoners', 8.2)
        # delete existing key
        tree.delete('Whiplash')
        assert tree.size == 2
        assert tree.contains('Whiplash') is False
        assert tree.contains('Parasite') is True
        assert tree.contains('Prisoners') is True

    def test_delete_nonexistent_raises_error(self):
        tree = AVLTree()
        tree.insert('Parasite', 8.5)
        with self.assertRaises(KeyError):
            tree.delete('Avatar')

    def test_delete_all(self):
        tree = AVLTree()
        tree.insert('Parasite', 8.5)
        tree.insert('Whiplash', 8.5)
        tree.delete('Parasite')
        tree.delete('Whiplash')
        assert tree.size == 0
        assert tree.is_empty() is True
        assert tree.root is None

    def test_items_in_order(self):
        tree = AVLTree()
        tree.insert('Parasite', 8.5)
        tree.insert('Whiplash', 8.5)
        tree.insert('Oddity', 6.7)
        tree.insert('The Prestige', 8.5)
        tree.insert('Prisoners', 8.2)
        items = tree.items_in_order()
        # should be in alpha order
        keys = [k for k, v in items]
        assert keys == ['Oddity', 'Parasite', 'Prisoners', 'The Prestige', 'Whiplash']

    def test_balance_after_insert(self):
        tree = AVLTree()
        # insert in sorted order (would be worst case for regular bst)
        tree.insert('A', 1)
        tree.insert('B', 2)
        tree.insert('C', 3)
        tree.insert('D', 4)
        tree.insert('E', 5)
        # tree should still be balanced — height should be ~3 not 5
        assert tree._height(tree.root) <= 3
        # all items should still be there
        assert tree.size == 5

    def test_balance_after_delete(self):
        tree = AVLTree()
        tree.insert('B', 2)
        tree.insert('A', 1)
        tree.insert('D', 4)
        tree.insert('C', 3)
        tree.insert('E', 5)
        tree.delete('A')
        # tree should rebalance after deletion
        bf = tree._balance_factor(tree.root)
        assert -1 <= bf <= 1

    def test_len(self):
        tree = AVLTree()
        assert len(tree) == 0
        tree.insert('Parasite', 8.5)
        assert len(tree) == 1
        tree.insert('Whiplash', 8.5)
        assert len(tree) == 2
        tree.delete('Parasite')
        assert len(tree) == 1


if __name__ == '__main__':
    unittest.main()
