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
   
    def append(self,item):
        newValue=Node(item)
        
        if self.head is None:
            self.head=newValue
            return 
        
        last=self.head
        while(last.next):
            last=last.next
        last.next=newValue
        
    def insertBefore(self,value, newVal):
        if self.head is None:
            raise ValueError('Linked List is Empty')
            
        newValue=Node(newVal)
        if self.head.value==value:
            newValue.next=self.head
            self.head=newValue
            return 
        
        last=self.head
        while(last.next):
            if last.next.value==value:
                newValue.next=last.next
                last.next=newValue
                return 
            else :
                last=last.next

        if last.next is None :
            raise ValueError('Node not is LL')   
        

    def insertAfter(self,value, newVal):
        if self.head is None:
            raise ValueError('Linked List is Empty')
            
        newValue=Node(newVal)
        last=self.head
        while(last):
            if last.value==value:
                newValue.next=last.next
                last.next=newValue
                return 
            else :
                last=last.next
       
        if last is None :
            raise ValueError('Node not is LL') 
     

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
        item.append(5)
        item.append(2)
        item.append(6)
        item.insertAfter(5,77)
        item.insertBefore(5,1)

    
        print(item.includes(2))
        print('Linked list:')
        str(item)
            
      