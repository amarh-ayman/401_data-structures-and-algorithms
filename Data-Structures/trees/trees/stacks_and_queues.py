class Node: 
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        
    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        
    def pop(self):
        if not self.is_empty():
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
        else:
            self.top = None
            raise ValueError("Empty LL") 
            
    def peek(self):
        if not self.is_empty():
            return self.top.value
        else:
            raise ValueError("Empty LL") 

    def is_empty(self): 
        return self.top == None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, value):
        node = Node(value)
        
        if not self.front:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if  self.is_empty():
            raise ValueError("Empty")
        else:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value
    def peek(self):
        if  self.is_empty():
            raise ValueError("Empty")
        else:
            return self.front.value
    def is_empty(self):
        return self.front == None
 