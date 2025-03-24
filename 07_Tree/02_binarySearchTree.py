class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self, root):
        self.root = None
    def insert(self,data):
        self.root = self.recursiveInsert(self, root, data)
    def recursiveInsert(self, root, data):
        if root is None:
            return Node(data)
        if data  < root.item:
            root.left = self.recursiveInsert(root.left, data)
        elif data > root.item:
            root.right = self.recursiveInsert(root.right, data)
        return root