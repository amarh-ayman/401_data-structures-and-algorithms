from trees.tree import Tree,Node
import pytest

def test_preOrder(data):
  assert data.preOrder()=='1243'

def test_inOrder(data):
  assert data.inOrder()=='4213'

def test_postOrder(data):
  assert data.postOrder()=='4231'

def test_Empty():
  tree=Tree()
  assert tree.preOrder()=='None'
  assert tree.inOrder()=='None'
  assert tree.postOrder()=='None'


@pytest.fixture
def data():
  tree =Tree()
  tree.root = Node(1)
  tree.root.left = Node(2)
  tree.root.right = Node(3)
  tree.root.left.left = Node(4)
  return tree
