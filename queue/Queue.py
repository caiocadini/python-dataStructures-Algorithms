from Node import Node

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, data):
        newNode = Node(data)
        if(self.size == 0):
            self.first = self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.size += 1
    
    def dequeue(self):
        if(self.size == 0):
            return None
        removeNode = self.first
        if(self.size == 1):
            self.first = self.last = None
        else:
            self.first = self.first.next
        self.size -= 1
        return removeNode
    
    def isEmpty(self):
        if(self.size == 0):
            return True
        return False
    
    def size(self):
        return self.size
    
    def clear(self):
        while(self.size != 0):
            print(f'removed element: {self.dequeue().data}')

    def printQueue(self):
        temp = self.first
        while(temp != None):
            print(temp.data)
            temp = temp.next
    

    

