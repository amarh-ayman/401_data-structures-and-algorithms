import sys
sys.path.append('Data-Structures/trees/trees')
from trees.BinarySearchTree import *

def treeIntersection(tree1,tree2):
    t1=tree1.preOrder()
    t2=set(tree2.preOrder())
    treeArray=[]
    for item in t1:
        if item in t2 :
            treeArray.append(item)
            
    return treeArray
    

# tree1 = BinarySearchTree()
# tree1.Add(23)
# tree1.Add(8)
# tree1.Add(42)
# tree1.Add(4)
# tree1.Add(16)
# tree1.Add(27)


# tree2 = BinarySearchTree()
# tree2.Add(100)
# tree2.Add(8)
# tree2.Add(42)
# tree2.Add(7)
# tree2.Add(16)
# tree2.Add(9)

# print(tree1.preOrder())
# print(treeIntersection(tree1,tree2))
