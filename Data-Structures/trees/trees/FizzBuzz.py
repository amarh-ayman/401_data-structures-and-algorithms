from trees.stacks_and_queues import Queue

class KNode :
    def __init__(self,v):
         self.value=v
         self.child=[None]*KNode.k
        
        

class K_Tree :
    def __init__(self,k):
        self.root=None
        KNode.k=k
       


def fizzBuzz(Ktree):
    queue=Queue()
    treees=[]
    treeWithoutBuzzing=[]
    count=0

    if not Ktree.root :
      return 'Empty'
   
    def _closure(node):
        nonlocal count
        
        try:
          if node.value %3 ==0 and node.value%5==0:
              node.value ='FizzBuzz'
          elif node.value %3 == 0 :
              node.value ='Fizz'
          elif node.value %5 == 0 :
              node.value ='Buzz'
          else :
              node.value=str(node.value)
          
          while KNode.k> count and node.child[count]:
              queue.enqueue(node.child[count])
              count+=1
          treees.append(node.value)

          if queue.front :
              node =queue.dequeue()
              treeWithoutBuzzing.append(node.value)
              count=0
              _closure(node) 
        except:
          return 'Error'      
                                
            
    
    treeWithoutBuzzing.append(Ktree.root.value)        
    _closure(Ktree.root)   
    return (treeWithoutBuzzing ,treees)
    
        
        
        

# t=K_Tree(3)
# t.root=KNode(1)
# t.root.child[0]=KNode(200)
# t.root.child[0].child[0]=KNode(12)
# t.root.child[0].child[1]=KNode(21)
# t.root.child[0].child[2]=KNode(3)


# t.root.child[1]=KNode(20)
# t.root.child[1].child[0]=KNode(30)
# t.root.child[1].child[1]=KNode(3)

# t.root.child[2]=KNode(9)
