class Node:
    def __init__(self,node):
        self.node=node
        self.adjecency_list=[]

class Edge:
    def __init__(self,start,end,weight=0):
        self.start=start
        self.end=end
        self.weight=weight
    def get_edge(self):
        edge=(self.start,self.end)

        return edge
class Graph:

    def __init__(self):
       self.nodeList=[]

       self.dict = {}
       self.edge_list = []


    def undirected_graph(self,tuple):
        for start, end in tuple:
            self.dict.setdefault(start, []).append(end)
            self.dict.setdefault(end, []).append(start)

        return self.dict
    def directed_graph(self,tuple):
        for start, end in tuple:
            self.dict.setdefault(start, []).append(end)

        return self.dict
    def display_graph(self):
        print(self.dict)
    def add_edge(self,start,end,weight=0):
        edge=Edge(start,end)
        edge=edge.get_edge()
        if start in self.nodeList:
           if end in self.nodeList:
            self.edge_list.append(edge)



        return self.dict
    def get_nodeList(self):
        return self.nodeList

    def add_node(self, node):

        self.nodeList.append(node)
        self.dict[node]=[]

        return self.nodeList


graph=Graph()
graph.add_node(4)
graph.add_node(2)
graph.add_edge(2,4,5)

graph.add_node(9)
graph.add_node(8)
graph.add_edge(9,8)
graph.add_node(6)
graph.add_node(4)
graph.add_edge(6,4)
graph.add_edge(4,3,weight=3)

graph.directed_graph(graph.edge_list)
graph.display_graph()
graph.undirected_graph(graph.edge_list)
graph.display_graph()
print(graph.get_nodeList())








