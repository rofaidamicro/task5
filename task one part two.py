import matplotlib.pyplot as plt
import networkx as nx

# --- Node Class ---
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

# --- BinarySearchTree Class ---
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        elif key > node.value:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.value == key:
            return node
        if key < node.value:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.value:
            node.left = self._delete(node.left, key)
        elif key > node.value:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete(node.right, temp.value)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.value)
            self._inorder_traversal(node.right, result)

# --- Tree Visualization Function ---
def plot_tree(tree):
    G = nx.DiGraph()
    positions = {}
    labels = {}

    def add_edges(node, pos_x=0, pos_y=0, level=1):
        if node:
            G.add_node(node.value)
            labels[node.value] = node.value
            positions[node.value] = (pos_x, pos_y)
            if node.left:
                G.add_edge(node.value, node.left.value)
                add_edges(node.left, pos_x - 1 / level, pos_y - 1, level + 1)
            if node.right:
                G.add_edge(node.value, node.right.value)
                add_edges(node.right, pos_x + 1 / level, pos_y - 1, level + 1)

    add_edges(tree.root)
    nx.draw(G, positions, with_labels=True, node_size=2000, node_color="skyblue", font_size=10)
    plt.show()

# --- Execution of Operations ---
a = [49, 38, 65, 97, 60, 76, 13, 27, 5, 1]
b = [149, 38, 65, 197, 60, 176, 13, 217, 5, 11]
c = [49, 38, 65, 97, 64, 76, 13, 77, 5, 1, 55, 50, 24]

# Create an instance of the BST
tree = BinarySearchTree()

# Insert elements from list a
for num in a:
    tree.insert(num)
    
# Visualize the tree after inserting list a
plot_tree(tree)
print("Inorder traversal of tree after inserting list a:", tree.inorder_traversal())

# Insert elements from list b
for num in b:
    tree.insert(num)

# Visualize the tree after inserting list b
plot_tree(tree)
print("Inorder traversal of tree after inserting list b:", tree.inorder_traversal())

# Insert elements from list c
for num in c:
    tree.insert(num)

# Visualize the tree after inserting list c
plot_tree(tree)
print("Inorder traversal of tree after inserting list c:", tree.inorder_traversal())

# Search for a value (e.g., 97)
search_result = tree.search(97)
print(f"Search result for 97: {'Found' if search_result else 'Not Found'}")

# Delete a value (e.g., 27)
tree.delete(27)
plot_tree(tree)
print("Inorder traversal of tree after deleting 27:", tree.inorder_traversal())
# Lists a, b, and c
a = [49, 38, 65, 97, 60, 76, 13, 27, 5, 1]
b = [149, 38, 65, 197, 60, 176, 13, 217, 5, 11]
c = [49, 38, 65, 97, 64, 76, 13, 77, 5, 1, 55, 50, 24]

# Create an instance of the BST
tree = BinarySearchTree()

# Insert elements from list a
for num in a:
    tree.insert(num)
    
# Visualize the tree after inserting list a
tree.plot()
print("Inorder traversal of tree after inserting list a:", tree.inorder_traversal())

# Insert elements from list b
for num in b:
    tree.insert(num)

# Visualize the tree after inserting list b
tree.plot()
print("Inorder traversal of tree after inserting list b:", tree.inorder_traversal())

# Insert elements from list c
for num in c:
    tree.insert(num)

# Visualize the tree after inserting list c
tree.plot()
print("Inorder traversal of tree after inserting list c:", tree.inorder_traversal())

# Search for the value 97
search_result = tree.search(97)
print(f"Search result for 97: {'Found' if search_result else 'Not Found'}")

# Delete the value 27
tree.delete(27)

# Visualize the tree after deleting 27
tree.plot()
print("Inorder traversal of tree after deleting 27:", tree.inorder_traversal())
