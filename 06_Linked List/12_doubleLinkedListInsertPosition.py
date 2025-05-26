class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    def insertPosition(self, data, pos):
        n = Node(data)
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        n.prev = temp
        n.next = temp.next
        temp.next.prev = n
        temp.next = n

