from hashTable.hashtable import Hashtable

def test ():
  pass

def test_hash_create():
    ht = Hashtable(10)
    assert ht.map == [None, None, None, None, None, None, None, None, None, None]

def test_hash_add():
    ht = Hashtable(1024)
    ht.add('name', 'amarh')
    keyHashed =ht.hash('name')
    assert ht.map[keyHashed].head.value == ('name', 'amarh')
    

def test_hash_get():
    ht = Hashtable(1024)
    ht.add('name', 'amarh')
    assert ht.get('name') == 'amarh'

def test_hash_get_not():
    ht = Hashtable(1024)
    assert ht.get('name') == None

def test_hash_add_collision():
    ht = Hashtable(1024)
    ht.add('name', 'amarh')
    ht.add('mane', 'not amarh')
    assert ht.get('name') == 'amarh'
    assert ht.get('mane') == 'not amarh'

def test_hash_hash():
    ht = Hashtable(1024)
    key = 'name'
    assert ht.hash(key) == 491

def test_hash_contains():
    ht = Hashtable(1024)
    ht.add('name', 'amarh')
    assert ht.contains('name') == True
    assert ht.contains('phone') == False
