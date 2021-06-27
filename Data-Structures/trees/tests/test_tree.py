from Binary_tree.BinaryTree import *
from Binary_tree.BinarySearchTree import *
import pytest

def test_preOrder(data):
  assert data.preOrder()=='1243'

def test_inOrder(data):
  assert data.inOrder()=='4213'

def test_postOrder(data):
  assert data.postOrder()=='4231'

def test_Empty():
  tree=BinaryTree()
  assert tree.preOrder()=='None'
  assert tree.inOrder()=='None'
  assert tree.postOrder()=='None'

def test_add_BinarySearchTree():
  tree=BinarySearchTree()
  tree.Add(6)
  assert tree.root.value==6
  tree.Add(10)
  assert tree.root.right.value==10
  tree.Add(3)
  assert tree.root.left.value==3
  tree.Add(30)
  assert tree.root.right.right.value==30


def test_BinarySearchTree_withBinaryTreeFunctions():
    tree = BinarySearchTree()
    tree.Add(5)
    tree.Add(10)
    tree.Add(4)
    assert tree.preOrder() == "5410"
    assert tree.inOrder() == "4510"
    assert tree.postOrder() == "4105"

def test_contain(data2):
  assert data2.contain(3)==True
  assert data2.contain(113)==False

def test_maximumNumber(data,data2):
  assert data.max()==4
  assert data.max()==30
  tree =BinaryTree()
  assert tree.max()=='there is an Error'

@pytest.fixture
def data():
  tree =BinaryTree()
  tree.root = Node(1)
  tree.root.left = Node(2)
  tree.root.right = Node(3)
  tree.root.left.left = Node(4)
  return tree

@pytest.fixture
def data2():
  tree=BinarySearchTree()
  tree.Add(6)
  tree.Add(10)
  tree.Add(3)
  tree.Add(30)
  return tree
