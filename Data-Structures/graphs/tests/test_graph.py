from graphs.graphs import *
import pytest

# Node can be successfully added to the graph

#  graph with only one node and edge can be properly returned
def test_add_node():
    graph = Graph()
    assert graph.add_node('a').value == 'a'

# The proper size is returned, representing the number of nodes in the graph
def test_size_empty():
    graph = Graph()
    assert graph.size() == 0


def test_size():
    graph = Graph()
    graph.add_node('a')
    assert graph.size() == 1

    graph.add_node('b')
    assert graph.size() == 2


def test_edge_start_node_not_in_graph():
    graph = Graph()
    start = Vertix('start')
    end = graph.add_node('end')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)

def test_edge_end_node_not_in_graph():
    graph = Graph()
    end = Vertix('end')
    start = graph.add_node('start')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)
# An edge can be successfully added to the graph
def test_add_one_edge():
    graph = Graph()
    end = graph.add_node('end')
    start = graph.add_node('start')
    graph.add_edge(start, end)

def test_add_edge():
    graph = Graph()
    end = graph.add_node('a')
    start = graph.add_node('b')
    graph.add_edge(start, end)
    assert graph.adjacency_list[start][0].vertix.value == end.value
    assert graph.adjacency_list[start][0].weight == 1
    assert graph.get_neighbors(start)[0].vertix.value == end.value
    graph.add_edge(end, start)
    assert graph.get_neighbors(end)[0].vertix.value == start.value

# A collection of all nodes can be properly retrieved from the graph
def test_get_nodes():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    assert len(graph.get_nodes()) == 2

# An empty graph properly returns null
def test_get_empty_NULL():
    graph = Graph()
    assert graph.get_nodes()=='NULL'

# All appropriate neighbors can be retrieved from the graph
# Neighbors are returned with the weight between nodes included

def test_get_neighbors():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    graph.add_edge(a, b, 5)
    neighbors = graph.get_neighbors(a)
    assert len(neighbors) == 1
    assert neighbors[0].vertix.value == 'b'
    assert isinstance(neighbors[0], Edge)
    assert neighbors[0].weight == 5

def test_get_neighbors_no_neighbors():
    g = Graph()
    c = g.add_node('c')
    assert g.size()==1
    neighbors = g.get_neighbors(c)
    assert str(g)=='c\n'
    assert neighbors == 'Empty'

def test_breadth_first():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    graph.add_edge(a, c)
    graph.add_edge(a, d)
    graph.add_edge(b, c)
    graph.add_edge(b, f)
    graph.add_edge(c, a)
    graph.add_edge(c, b)
    graph.add_edge(c, e)
    graph.add_edge(d, a)
    graph.add_edge(d, e)
    graph.add_edge(e, c)
    graph.add_edge(e, d)
    graph.add_edge(e, f)
    graph.add_edge(f, b)
    graph.add_edge(f, e)


    breadth = graph.breadth_first(a)
    assert len(breadth) == 6
    assert breadth[0] == 'a'
    assert breadth[1] == 'c'
    assert breadth[2] == 'd'
    assert breadth[3] == 'b'
    assert breadth[4] == 'e'
  



    