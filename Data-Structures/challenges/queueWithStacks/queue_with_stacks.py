from stacks_and_queues.stacks_and_queues import Stack

class PseudoQueue:
    def __init__(self):
        self.pushStack = Stack()
        self.popStack = Stack()

    def enqueue(self, item):
        self.pushStack.push(item)

    def dequeue(self):
        if self.popStack.is_empty():
            while self.pushStack.top != None:
                self.popStack.push(self.pushStack.pop())
                
        return self.popStack.pop()
        

my_queue = PseudoQueue()
my_queue.enqueue(10)
my_queue.enqueue(15)
my_queue.enqueue(20)
my_queue.enqueue(5)

print(my_queue.dequeue())
print(my_queue.dequeue())
# print(my_queue.dequeue())
# print(my_queue.dequeue())

 