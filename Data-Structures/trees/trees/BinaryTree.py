class Node:
    def __init__(self,val):
        self.value=val
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None
        
    def preOrder(self):
        def __pre(root):
            if root is None:
                return []
            else :
                return [root.value]+__pre(root.right)+__pre(root.left)
        return __pre(self.root)        

    def inOrder(self):
        def __in(root):
            if root is None:
                return []
            else :
                return __in(root.right)+[root.value]+__in(root.left)
        return __in(self.root)        
       
    def postOrder(self):
        def __post(root):
            if root is None:
                return []
            else :
                return __post(root.right)+__post(root.left)+[root.value]
        return __post(self.root)    
   
    def max(self):
        if not self.root :
            return 'Empty Tree'
        def __maximum(root,maxi=0):
            if root.left:
                maxi=__maximum(root.left,maxi)
        
            if root.right:
                maxi=__maximum(root.right,maxi) 
                
            if root.value > maxi :
                maxi=root.value 
        
            return maxi  
        return __maximum(self.root)         
        
                
            
            
            

# tree =BinaryTree()
# tree.root = Node(1)

# tree.root.left = Node(200)
# tree.root.right = Node(3)

# tree.root.left.left = Node(4)
# tree.root.left.right = Node(50)
# tree.root.right.right = Node(100)


# print("Pre order : ", end="")
# print(tree.preOrder())  
# print(tree.max()) 

# print(tree.inOrder()) 
# print(tree.postOrder()) 
            
        