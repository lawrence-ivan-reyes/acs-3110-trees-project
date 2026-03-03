# AVL Tree Movie Database

A movie database CLI app built on a self-balancing AVL tree. 

## Project Structure

```
├── avl_tree.py        # core avl tree with rotations and rebalancing
├── tree_map.py        # ordered map adt backed by avl tree
├── movie_db.py        # interactive movie database cli
├── avl_tree_test.py   # unit tests
├── movies.csv         # dataset of 30 movies
└── README.md
```

## How It Works

The project is layered:

1. **AVL Tree** (`avl_tree.py`): self-balancing binary search tree supporting insert, search, delete, and in-order traversal. All operations are O(log n).
2. **Ordered Tree Map** (`tree_map.py`): a dict-like interface backed by the AVL tree. Keys are always sorted.
3. **Movie Database** (`movie_db.py`): loads movies from CSV into two tree maps (by title and by rating). Supports search, browse, genre filter, and top-rated queries.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
```

## Usage

Run the movie database:
```bash
python movie_db.py
```

Run the AVL tree demo:
```bash
python avl_tree.py
```

Run tests:
```bash
python -m unittest avl_tree_test -v
```
