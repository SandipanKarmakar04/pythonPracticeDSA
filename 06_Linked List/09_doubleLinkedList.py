class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    def display(self):
        if self.head is None:
            print("Empty!")
        else:
            temp = self.head
            while temp:
                print(temp.data,end=" -->")
                temp = temp.next

dLL = DoubleLinkedList()
node = Node(10)
dLL.head = node
dLL.display()