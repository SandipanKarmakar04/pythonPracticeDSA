class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")
    def deletionBegining(self):
        current = self.head
        self.head = current.next
        current.next = None

l = LinkedList()

l.append(10)
l.append(20)
l.append(30)
l.display()

l.deletionBegining()
l.display()