class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
    
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

tree = BinaryTree("A")
tree.root.left = Node("B")
tree.root.right = Node("C")
tree.root.right.left = Node("D")
tree.root.right.right = Node("E")

print("Preorder traversal:")
tree.preorder(tree.root)

print("\nInorder traversal:")
tree.inorder(tree.root)

print("\nPostorder traversal:")
tree.postorder(tree.root)