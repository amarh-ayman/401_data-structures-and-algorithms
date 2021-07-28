from trees.BinarySearchTree import *

from Code_Challenges.ALgorithm.hashmap_tree_intersection import *

import pytest

def test_bothFull(data1,data2) :
  assert treeIntersection(data1,data2)==[8,42,16]
    

def test_Oneempty(data1):
  tree=BinarySearchTree()
  assert treeIntersection(data1,tree)==[]

def test_bothempty():
  tree=BinarySearchTree()
  tree2=BinarySearchTree()
  assert treeIntersection(tree,tree2)==[]
    
def test_notContain():
  tree=BinarySearchTree()
  tree.Add(1)
  tree.Add(12)
  tree.Add(31)
  tree2=BinarySearchTree()
  tree.Add(100)
  tree.Add(50)
  tree.Add(88)

  assert treeIntersection(tree,tree2)==[]


@pytest.fixture
def data1():
    tree1 = BinarySearchTree()
    tree1.Add(23)
    tree1.Add(8)
    tree1.Add(42)
    tree1.Add(4)
    tree1.Add(16)
    tree1.Add(27)
    return tree1

@pytest.fixture
def data2():  
    tree2 = BinarySearchTree()
    tree2.Add(100)
    tree2.Add(8)
    tree2.Add(42)
    tree2.Add(7)
    tree2.Add(16)
    tree2.Add(9)   
    return tree2 
