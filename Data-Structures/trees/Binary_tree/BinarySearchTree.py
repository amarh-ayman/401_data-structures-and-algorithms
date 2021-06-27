from Binary_tree.BinaryTree import *

class BinarySearchTree(BinaryTree):
    def Add(self ,key):
        if not self.root :
            self.root=Node(key)

        def insert(node):
            nonlocal key
            if key == node.value:
                return 'this value was added before'
            
            if key < node.value:
                if node.left is None :
                    node.left = Node(key)
                else :    
                    node.left = insert(node.left)
            else:
                if node.right is None :
                    node.right = Node(key)
                else :    
                    node.right = insert(node.right)
                    
            return node        
    
        insert(self.root)
                        
    def contain(self,key):
        def _cont(node):
            try:
                nonlocal key
                if key == node.value:
                    return True
                    
                if key < node.value:
                    return _cont(node.left)
                else:
                   return _cont(node.right)
            except:   
                return False   
                
        return _cont(self.root)

    
tree = BinarySearchTree()
tree.Add(23)
tree.Add(8)
tree.Add(42)
tree.Add(4)
tree.Add(16)
tree.Add(27)

print(tree.contain(30))
