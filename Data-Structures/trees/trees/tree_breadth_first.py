from trees.BinaryTree import *
from trees.stacks_and_queues import Queue

def breadthFirst(self):
        self.queue=Queue()
        self.print=[]
        if not self.root:
            return 'Empty'

        if self.root:
            self.queue.enqueue(self.root)
        val=self.queue.dequeue() 
        self.print.append(val.value)

        def _breadth(node):
            if node.left:
                self.queue.enqueue(node.left)

            if node.right:
                self.queue.enqueue(node.right)
            
            if  self.queue.front :
                 val=self.queue.dequeue() 
                 self.print.append(val.value) 
                 _breadth(val)
                 
        _breadth(val)         
        return self.print

        




# tree = BinaryTree()
# tree.root = Node(1)

# tree.root.left = Node(200)
# tree.root.right = Node(3)

# tree.root.left.left = Node(4)
# tree.root.left.right = Node(50)
# tree.root.right.right = Node(100)

# print(breadthFirst(tree))