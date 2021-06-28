from trees.tree_breadth_first import *
from trees.BinaryTree import *
import pytest 

def test_breadthFirst01(data):
  assert breadthFirst(data)==[1, 200, 3, 4, 50,100]

def test_breadthFirst02():
   tree = BinaryTree()
   tree.root = Node(1)
   assert breadthFirst(tree)==[1]
   tree.root.left = Node(2)
   tree.root.right = Node(3)
   assert breadthFirst(tree)==[1, 2, 3]


@pytest.fixture
def data():
  tree = BinaryTree()
  tree.root = Node(1)

  tree.root.left = Node(200)
  tree.root.right = Node(3)

  tree.root.left.left = Node(4)
  tree.root.left.right = Node(50)
  tree.root.right.right = Node(100)
  return tree


