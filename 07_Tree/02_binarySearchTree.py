class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self,data):
        self.root = self.recursiveInsert(self.root, data)
    def recursiveInsert(self, root, data):
        if root is None:
            return Node(data)
        if data  < root.data:
            root.left = self.recursiveInsert(root.left, data)
        elif data > root.data:
            root.right = self.recursiveInsert(root.right, data)
        return root
    def search(self, data):
        return self.recursiveSearch(self.root, data)
    def recursiveSearch(self, root, data):
        if root is None or root.item == data:
            return root
        elif data < root.data:
            return self.recursiveSearch(root.left, data)
        elif data > root.data:
            return self.recursiveSearch(root.right, data)
    def preorder(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)
    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")
    
bst = BinarySearchTree()

bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

# Traversals
print("Inorder Traversal:")
bst.inorder(bst.root)      # Output: 20 30 40 50 60 70 80

print("\nPreorder Traversal:")
bst.preorder(bst.root)     # Output: 50 30 20 40 70 60 80

print("\nPostorder Traversal:")
bst.postorder(bst.root)    # Output: 20 40 30 60 80 70 50
