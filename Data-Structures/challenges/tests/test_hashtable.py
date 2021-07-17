from hashTable.hashtable import Hashtable

def test ():
  pass

def test_addingToHashTable():
  hashtable = Hashtable()
  hashtable.add('ahmad', 25)
  hashtable.add('hamad', 29)
  assert len(set(hashtable.map))==2

def test_getValueAdded():
  hashtable = Hashtable()
  hashtable.add('ahmad', 25)
  hashtable.add('hamad', 29)
  assert hashtable.get('ahmad')==25

def test_contain():
  hashtable = Hashtable()
  hashtable.add('ahmad', 25)
  hashtable.add('hamad', 29)
  assert hashtable.contains('ahmad')==True
  assert hashtable.contains('am')=='Null'
  
def test_hash():
  hashtable = Hashtable()
  assert hashtable.hash('ab')==97  
