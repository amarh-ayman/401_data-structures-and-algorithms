from linked_list.llist import LinkedList,Node
from linked_list import __version__

def test_version():
    assert __version__ == '0.1.0'

def test_Node():
   test=Node('a')
   assert test.value=='a'
   assert test.next==None

def test_EmptyList():
   test01=LinkedList()
   test01.insert()
   expected=test01.head.value
   actual=None
   assert expected==actual


def test_insertionand_head ():
   test02=LinkedList()
   test02.insert(2)
   expected=test02.head.value
   actual= 2
   assert expected==actual


def test_multiInsertion():
    test03=LinkedList()
    test03.insert(2)
    test03.insert('b')
    test03.insert('m')
    test03.insert(5)
    expected=test03.toString()[1]
    actual= 4
    assert expected==actual

def test_findOut():
    test04=LinkedList()
    test04.insert(2)
    test04.insert('b')
    test04.insert('m')
    test04.insert(5)
    assert test04.includes(5)==True
    assert test04.includes(7)==False
    

def test_output():
    test05=LinkedList()
    test05.insert(2)
    test05.insert('b')
    test05.insert('m')
    test05.insert(5)
    expected=test05.toString()[0]
    actual='{ 5 } -> { m } -> { b } -> { 2 } ->NULL'
