class Queue:
    def __init__(self):
        self.items = []
        self.rear = None
        self.front = None
    def isEmpty(self):
        return len(self.items) == 0
    def insert(self, data):
        self.items.append(data)
    def delete(self):
        if not self.isEmpty():
            self.items.pop(0)
        else:
            raise IndexError("Queue is empty")
    def getFront(self):
        if not self.isEmpty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")
    def getRear(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise IndexError("Queue is empty")
q1 = Queue()
q1.insert(10)
q1.insert(20)
q1.insert(30)
print("Top element is:",q1.getFront())
print("Remove front element is:",q1.delete())