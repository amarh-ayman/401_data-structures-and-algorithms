##import from hash map
import sys
sys.path.append('/home/amarah/Software_development_~/401_data-structures-and-algorithms/Data-Structures/challenges/hashTable/')

from hashtable import Hashtable

def hashmap_left_join(data1,data2):
  output=[]
  for item in data1.map :
    if item:
      hashed=data2.hash(item.head.value[0])
      if data2.map[hashed]:
        item2=data2.map[hashed].head.value[1]
        output.append([item.head.value[0],item.head.value[1],item2])
  
  print(output)



synonym=Hashtable()
synonym.add('fond','enamored')
synonym.add('warth','anger')
synonym.add('diligent','employed')
synonym.add('outfit','garb')
synonym.add('guide','usher')


antonyms=Hashtable()
antonyms.add('fond','averse')
antonyms.add('warth','delight')
antonyms.add('diligent','idle')
antonyms.add('guide','follow')
antonyms.add('flow','jam')

hashmap_left_join(synonym,antonyms)