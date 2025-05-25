class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
    def isEmpty(self):
        return self.front == -1
    def isFull(self):
        return (self.rear + 1) % self.size == self.front
    def insert (self, data):
        if self.isFull():
            raise OverflowError("Queue is full")
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
    def remove(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        remove = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return remove
    def getFront(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        return self.queue[self.front]
    def getRear(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        return self.queue[self.rear]
    
cq = CircularQueue(8)
cq.insert(5)
cq.insert(7)
cq.insert(1)
cq.insert(3)
cq.insert(4)
cq.insert(9)
cq.insert(2)
cq.insert(6)

print(cq.getFront())
