from trees.FizzBuzz import *
import pytest


def test_kTree(data):
  assert data.root.child[0].child[2].value==3
  assert data.root.child[1].child[2]==None
  assert fizzBuzz(data)[0]==[1, 200, 20, 9, 12, 21, 3, 30, 3]

def test_fizzBuzz(data):
  assert fizzBuzz(data)[1]==['1', 'Buzz', 'Buzz', 'Fizz', 'Fizz', 'Fizz', 'Fizz', 'FizzBuzz', 'Fizz']


def test_fizzBuzz_02():
  t=K_Tree(6)
  t.root=KNode(10)
  t.root.child[0]=KNode(0)
  t.root.child[1]=KNode(1)
  t.root.child[2]=KNode(22)
  t.root.child[3]=KNode(13)
  t.root.child[4]=KNode(40)
  t.root.child[5]=KNode(15)

  t.root.child[5].child[0]=KNode(12)
  t.root.child[3].child[1]=KNode(21)
  t.root.child[2].child[2]=KNode(3)
  
  result=fizzBuzz(t)

  assert result[0]==[10, 0, 1, 22, 13, 40, 15, 12]
  assert result[1]==['Buzz', 'FizzBuzz', '1', '22', '13', 'Buzz', 'FizzBuzz', 'Fizz']

def test_fizzBuzz_Error_Empty():
  t=K_Tree(6)
  assert  fizzBuzz(t)=='Empty' 




@pytest.fixture
def data():
  t=K_Tree(3)
  t.root=KNode(1)
  t.root.child[0]=KNode(200)
  t.root.child[0].child[0]=KNode(12)
  t.root.child[0].child[1]=KNode(21)
  t.root.child[0].child[2]=KNode(3)


  t.root.child[1]=KNode(20)
  t.root.child[1].child[0]=KNode(30)
  t.root.child[1].child[1]=KNode(3)

  t.root.child[2]=KNode(9)
  return t

