from trees.BinaryTree import *
from trees.stacks_and_queues import Queue

def breadthFirst(tree):
        queue=Queue()
        printTree=[]
        if not tree.root:
            return 'Empty'

        printTree.append(tree.root.value)

        def _breadth(node):
            if node.left:
                queue.enqueue(node.left)

            if node.right:
                queue.enqueue(node.right)
            
            if  queue.front :
                 val=queue.dequeue() 
                 printTree.append(val.value) 
                 _breadth(val)
                 
        _breadth(tree.root)         
        return printTree

        




# tree = BinaryTree()
# tree.root = Node(1)

# tree.root.left = Node(200)
# tree.root.right = Node(3)

# tree.root.left.left = Node(4)
# tree.root.left.right = Node(50)
# tree.root.right.right = Node(100)

# print(breadthFirst(tree))