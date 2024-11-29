import heapq

class Graph:
    def __init__(self):
        self.adjacency_List = {}
    
    # Add a Node to the Graph:
    def add_node(self, node):
        if node not in self.adjacency_List:
            self.adjacency_List[node] = []

    # Add a weighted edge between two nodes:
    def add_edge(self, from_node, to_node, weight):
        self.add_edge(from_node)
        self.add_edge(to_node)
        self.adjacency_List[from_node].append((to_node, weight))
        self.adjacency_List[to_node].append((from_node,weight))
    
    # Find shortest path using Dijkstra's algorithm:
    def dijkstra(self, start,end):
        