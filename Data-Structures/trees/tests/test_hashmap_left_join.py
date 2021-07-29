from tests.test_hashmap_tree_intersection import data1
from Code_Challenges.ALgorithm.hashmap_left_join import hashmap_left_join
import sys
sys.path.append('/home/amarah/Software_development_~/401_data-structures-and-algorithms/Data-Structures/challenges/hashTable/')

from hashtable import Hashtable

def test_1_completed():
  data1=Hashtable()
  data1.add('fond','enamored')
  
  data2=Hashtable()
  data2.add('fond','averse')
  assert hashmap_left_join(data1,data2)==[['fond', 'enamored', 'averse']]


def test_2_noRight():
  data1=Hashtable()
  data1.add('fond','enamored')
  
  data2=Hashtable()
  data2.add('warth','anger')
  assert hashmap_left_join(data1,data2)==[['fond', 'enamored', 'NULL']]  

def test_3_noLeft():
  data1=Hashtable()
  
  data2=Hashtable()
  data2.add('warth','anger')
  assert hashmap_left_join(data1,data2)==[] 

  