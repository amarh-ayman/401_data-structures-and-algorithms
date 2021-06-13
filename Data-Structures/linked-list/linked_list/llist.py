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
        if self.head is None:
            return False
        else:
            item=self.head
            while(item):
                if(item.value==data):
                    return True
                else: 
                    item=item.next
            
            return False
            
    def __str__(self):
        if self.head is None:
            return 'Linked List is Empty'
        else :

            item=self.head
            s=''
            if item.value!=None:
                while(item):
                    s+=' { '+str(item.value)+' } ->'
                    item=item.next
                return s+'NULL'
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
            
      