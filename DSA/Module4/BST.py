'''Implement Binary Search tree with the following details:
Create a class node with the data members left, right, and key, and
constructor __init__(), to initialize the value of key
Create a class BnrySeacrchTree with the following members:
Data members root
Define constructor __init__() to initialize root with null value
Define a member function insert(self, value) to insert a new node in the
binary search tree
Define a member function delete(self) to delete a node from the binary
search tree.
Define a member function preorder() for preorder traversal
Define a member function postorder() for postorder traversal
Define a member function inorder() for inorder traversal
Define a member function hight to calculate height of the tree'''
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    else:
        return search(root.right, key)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)

def preorder(root):
    if root:
        print(root.key, end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=' ')

def find_min(node):
    current = node
    while current.left:
        current = current.left
    return current

def delete(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        # Node with one or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # Node with two children
        temp = find_min(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


root = None
values = [50, 30, 20, 40, 70, 60, 80]
for val in values:
    root = insert(root, val)

print("Inorder Traversal:")
inorder(root)

key = 60
found = search(root, key)
if found:
    print(f"\n{key} found in BST.")
else:
    print(f"\n{key} not found in BST.")


del_key = 50
print(f"\nDeleting {del_key}...")
root = delete(root, del_key)
print("Inorder after deletion:")
inorder(root)

print(f"\nHeight of BST: {height(root)}")
