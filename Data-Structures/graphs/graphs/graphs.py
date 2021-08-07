import sys
sys.path.append('/home/amarah/Software_development_~/401_data-structures-and-algorithms/Data-Structures/challenges/stacks_and_queues/')

from stacks_and_queues import Queue

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
                output += ' -'+ str(edge.weight)+'-> ' + edge.vertix.value 
            output+='\n'    
        return output

    def breadth_first(self,node):  
        queue=Queue()
        queue.enqueue(node)
        visited=set()
        visited.add(node)
        bfList=[]

        bfList.append(node.value)
        def __BFS(queue,visited,bfList):
            node=queue.dequeue()
            visited.add(node)
            neighbors=self.get_neighbors(node)
            for edge in neighbors:
                if edge.vertix not in visited :
                    queue.enqueue(edge.vertix)
                    visited.add(edge.vertix)
                    bfList.append(edge.vertix.value)
                    
            while not queue.is_empty():
                __BFS(queue,visited,bfList)
        
        __BFS(queue,visited,bfList)
        return bfList    

    def graph_business_trip(self,listOfCountries):
        country=self.get_neighbors(listOfCountries[0])
        count=0
        check=False
        for item in listOfCountries[1:] :
            for target in country :
                if item==target.vertix:
                    count+= target.weight
                    check=True

            country=self.get_neighbors(item)
        return [check,count]            








if __name__ == '__main__':
    graph = Graph()
    p = graph.add_node('Pandora')
    a = graph.add_node('Arendelle')
    m = graph.add_node('Metroville')
    nm = graph.add_node('New Monstropolis')
    no = graph.add_node('Naboo')
    nar = graph.add_node('Narnia')

    graph.add_edge(p, a, 150)
    graph.add_edge(p, m, 82)

    graph.add_edge(a, p , 150)
    graph.add_edge(a, nm ,42)
    graph.add_edge(a, m ,99)

    graph.add_edge(nm, a, 42)
    graph.add_edge(nm, no, 73)
    graph.add_edge(nm, m, 105)

    graph.add_edge(no, nm, 73)
    graph.add_edge(no, m, 26)
    graph.add_edge(no, nar, 250)
    
    graph.add_edge(nar, m, 37)
    graph.add_edge(nar, no, 250)

    graph.add_edge(m, p, 82)
    graph.add_edge(m, a, 99)
    graph.add_edge(m, nm, 105)
    graph.add_edge(m, no, 26)
    graph.add_edge(m, nar, 37)
    
    # print(graph)
    # if a in graph.adjacency_list[a]:
    #     print('**')
    # print(graph.adjacency_list[p])
    # for item in graph.adjacency_list[p] :
    #     if 'Arendelle' == item.vertix.value:
    #         print('***')
    #     print(item.vertix,' ',item.weight)
    
    # print(graph.get_nodes())
#     # print(graph.size())
    print(graph.graph_business_trip([a, nm, no]))
    print(graph.graph_business_trip([ no,p]))
    print(graph.graph_business_trip([nar,a,no]))
