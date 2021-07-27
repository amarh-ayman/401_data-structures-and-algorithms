from hashTable.llist import LinkedList

class Hashtable:
    def __init__(self, size=1024):
      self.size = size
      self.map = [None]*size

    def hash(self, key):
      sum_of_asccii = 0
      for ch in key:
          sum_of_asccii += ord(ch)
      hashed_key = (sum_of_asccii * 11) % self.size
      return hashed_key
    
    def add(self, key, value):
      hashed_key = self.hash(key)
      if not self.map[hashed_key]:
          self.map[hashed_key] = LinkedList()
      self.map[hashed_key].insert((key,value))
    
    def get(self,key):
      hashed_key = self.hash(key)
      if not self.map[hashed_key]:
        return None 

      ll=self.map[hashed_key].head
      while ll :
        if  ll.value[0]==key :
          return ll.value[1]
        ll=ll.next 

      return None 
        
    
    def contains(self,key):
      hashed_key = self.hash(key)
      try:
          ll=self.map[hashed_key].head
      except :
        return False 

      while ll :
        if  ll.value[0]==key :
          return True
        ll=ll.next
      return False  
    



        

