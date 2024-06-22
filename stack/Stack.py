from Node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    def push(self, data: int):
        #Stack is empty
        if(self.size == 0):
            self.top = Node(data)
        else:
            newNode = Node(data)
            newNode.next = self.top
            self.top = newNode
        
        self.size += 1
    def pop(self):
        if(self.size == 0):
            return None
        removedNode = self.top
        self.top = self.top.next
        self.size -= 1
        return removedNode
    def peek(self):
        return self.top
    def isEmpty(self):
        if(self.size == 0):
            return True
        return False
    def printStack(self):
        readNode = self.top
        while(readNode != None):
            print(readNode.data)
            readNode = readNode.next