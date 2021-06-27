class Node:
    def __init__(self,val):
        self.value=val
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None
        self.print=''
        self.pre=True
        self.inO=True
        self.post=True
    
    def preOrder(self):
        if self.pre :
            self.print=''
            self.pre=False
            
        if not self.root:
            return 'None'
       
        def _order(node):
            self.print+=str(node.value)
            if node.left:
                _order(node.left)
            if node.right:
                _order(node.right)
        _order(self.root)
        return self.print
    
    def inOrder(self):
        if self.inO :
            self.print=''
            self.inO=False
            
        if not self.root:
            return 'None'
       
        def _order(node):
            if node.left:
                _order(node.left)
            self.print+=str(node.value)    
            if node.right:
                _order(node.right)
        _order(self.root)
        return self.print 
    
    def postOrder(self):
        if self.post :
            self.print=''
            self.post=False
            
        if not self.root:
            return 'None'
       
        def _order(node):
            if node.left:
                _order(node.left)
            if node.right:
                _order(node.right)
            self.print+=str(node.value)    
        _order(self.root)
        return self.print
        
    @classmethod
    def printing(cls):
        return cls.print

    def max(self):
        
        try:
            maximum=0
            def _max(node):
                nonlocal maximum
                if node.value > maximum :
                    maximum=node.value

                if node.left:
                    _max(node.left)
                if node.right:
                    _max(node.right) 
            
            _max(self.root)
            return maximum
        except:
            return 'there is an Error'            
        


                
            
            
            

tree =BinaryTree()
# tree.root = Node(1)

# tree.root.left = Node(200)
# tree.root.right = Node(3)

# tree.root.left.left = Node(4)
# tree.root.left.right = Node(50)
# tree.root.right.right = Node(100)


# print("Pre order : ", end="")
# print(tree.preOrder())  
print(tree.max()) 

# print(tree.inOrder()) 
# print(tree.postOrder()) 
            
        