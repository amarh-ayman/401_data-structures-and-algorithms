from linked_list.llist import LinkedList,Node
from linked_list import __version__
import pytest
<<<<<<< HEAD
=======

>>>>>>> 08797bc080c81f006521c8e9333285507056f5d6
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


def test_insertBefore_01(data):
   data.insertBefore('a',7)
   assert data.head.value is 7

def test_insertBefore_02(data):
   data.insertBefore(10,7)
   assert data.head.next.value is 7

def test_insertBefore_03(data):
   data.insertBefore(6,'m')
   assert data.head.next.next.value is 'm'   

def test_insertBefore_04(data):
   with pytest.raises(ValueError):
      data.insertBefore('c',7)   

###############
def test_insertAfter_01(data):
   data.insertAfter('a',7)
   assert data.head.next.value is 7

def test_insertAfter_02(data):
   data.insertAfter(10,7)
   assert data.head.next.next.value is 7

def test_insertAfter_03(data):
   data.insertAfter(6,7)
   assert data.head.next.next.next.value is 7  

def test_insertAfter_04(data):
   with pytest.raises(ValueError):
      data.insertAfter('c',7)   
# ===============================
def test_kthFromTheEnd_01(data):
   with pytest.raises(ValueError):
      data.kthFromTheEnd(7) 

def test_kthFromTheEnd_02(data):
   with pytest.raises(ValueError):
      data.kthFromTheEnd(3)

def test_kthFromTheEnd_03(data):
   with pytest.raises(ValueError):
      data.kthFromTheEnd(-7)  

def test_kthFromTheEnd_04(data02):
   expected=data02.kthFromTheEnd(0)
   assert data02.head.value==expected

def test_kthFromTheEnd_05(data):
   expected=data.kthFromTheEnd(1)
   assert data.head.next.value==expected    

@pytest.fixture
def data():
   ll=LinkedList()
   ll.append('a')
   ll.append(10)
   ll.append(6)
   return ll

@pytest.fixture
def data02():
   ll=LinkedList()
   ll.append(1)
   return ll


    
