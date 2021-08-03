class Vertix:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f'Vertix > {self.value}'

class Edge:
    def __init__(self, vertix , weight):
        self.vertix = vertix
        self.weight = weight

class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_node(self, value):
        v = Vertix(value)
        self.adjacency_list[v] = []
        return v
    
    def add_edge(self, start_node, end_node, weight=1):
        if start_node==end_node :
          raise 'you try to connect same node'
        if start_node not in self.adjacency_list or end_node not in self.adjacency_list :  
          raise KeyError('not exist')  

        edge = Edge(end_node, weight)
        self.adjacency_list[start_node].append(edge)
    
    def get_nodes(self):
        if not self.adjacency_list:
            return 'NULL'
        return self.adjacency_list.keys() 
    
    def get_neighbors(self, node):
        if not len(self.adjacency_list[node]):
            return 'Empty'
        return self.adjacency_list[node]
    
    def size(self):
        return len(self.adjacency_list)

    def __str__(self):
        output = ''
        for vertix in self.adjacency_list.keys():
            output += vertix.value
            for edge in self.adjacency_list[vertix]:
                output += ' -> ' + edge.vertix.value 
            output+='\n'    
        return output

    def breadth_first(self,node):  
        queue=[]
        queue.append(node)
        visited=[]
        visited.append(node)
        bfList=[]
  
        def __BFS(queue,visited,bfList):
            node=queue.pop(0)
            visited.append(node)
            bfList.append(node.value)
            neighbors=self.get_neighbors(node)
            for edge in neighbors:
                if edge.vertix not in visited :
                    queue.append(edge.vertix)
                    visited.append(edge.vertix)
                    bfList.append(edge.vertix.value)
                    
            if len(queue):
                __BFS(queue,visited,bfList)
        
        __BFS(queue,visited,bfList)
        return bfList    




if __name__ == '__main__':
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

#     # # print(graph)
#     # # print(graph.adjacency_list)
#     # print(graph.get_nodes())
#     # print(graph.size())
    print((graph.breadth_first(a)))
