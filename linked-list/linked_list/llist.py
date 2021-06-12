class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert(self ,data=None):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
        
    def includes(self,data):
        item=self.head
        while(item):
            if(item.value==data):
                return True
            else: 
                item=item.next
        
        return False
            
    def toString(self):
        item=self.head
        s=''
        count=0
        if item.value!=None:
            while(item):
                count +=1
                s+=' { '+str(item.value)+' } ->'
                item=item.next
            return [s+'NULL',count]
        else:
            return 

if __name__ == '__main__':
        item = LinkedList()
        item.insert(22223)
        item.insert('3')
        item.insert(2)
        item.insert(3)
        item.insert(3)
        print(item.includes(2))
        print('Linked list:')
        item.toString()
            
      