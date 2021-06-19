
from ll_zip.ll_zip import zipping
from ll_zip.llist import LinkedList
import pytest

def test_zippingEmpty_01():
  Empty01=LinkedList()
  Empty02=LinkedList()
  zipping(Empty01,Empty02)
  assert str(Empty01)=='Linked List is Empty'
  assert str(Empty02)=='Linked List is Empty'

def test_zippingEmpty_02(data01):
  Empty01=LinkedList()
  zipping(data01,Empty01)
  assert str(data01)==' { a } -> { 10 } -> { 6 } ->NULL'
  assert str(Empty01)==' { a } -> { 10 } -> { 6 } ->NULL'

def test_zippingAllFullNotEqualLength(data01,data02):
  zipping(data01,data02)
  assert str(data01)==' { a } -> { 1 } -> { 10 } -> { 2 } -> { 6 } -> { 3 } -> { 4 } ->NULL'
  assert str(data02)==' { 1 } -> { 10 } -> { 2 } -> { 6 } -> { 3 } -> { 4 } ->NULL'

def test_zippingAllFullEqualLength(data01,data03):
  zipping(data01,data03)
  assert str(data01)==' { a } -> { c } -> { 10 } -> { v } -> { 6 } -> { b } ->NULL'
  assert str(data03)==' { c } -> { 10 } -> { v } -> { 6 } -> { b } ->NULL'




@pytest.fixture
def data01():
   ll=LinkedList()
   ll.append('a')
   ll.append(10)
   ll.append(6)
   return ll

@pytest.fixture
def data02():
   ll=LinkedList()
   ll.append(1)
   ll.append(2)
   ll.append(3)
   ll.append(4)
   return ll

@pytest.fixture
def data03():
   ll=LinkedList()
   ll.append('c')
   ll.append('v')
   ll.append('b')
   return ll





