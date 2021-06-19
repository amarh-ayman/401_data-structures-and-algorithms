from linked_list.llist import LinkedList,Node
from linked_list import __version__
import pytest
def test_version():
    assert __version__ == '0.1.0'

def test_Node():
   test=Node('a')
   assert test.value=='a'
   assert test.next==None

def test_EmptyList():
   test01=LinkedList()
   assert test01.head is None


def test_insertionand_head ():
   test02=LinkedList()
   test02.insert(2)
   test02.insert(5)
   test02.insert('a')
   assert test02.head.value is 'a'
   assert test02.head.next.value is 5
   assert test02.head.next.next.value is 2


def test_findOut():
    test04=LinkedList()
    test04.insert(2)
    test04.insert('b')
    test04.insert('m')
    test04.insert(5)
    assert test04.includes(5) is True
    assert test04.includes(7) is False
    

def test_output():
    test05=LinkedList()
    test05.insert(2)
    test05.insert('b')
    test05.insert('m')
    test05.insert(5)
    expected=str(test05)
    actual=' { 5 } -> { m } -> { b } -> { 2 } ->NULL'
    assert expected==actual
