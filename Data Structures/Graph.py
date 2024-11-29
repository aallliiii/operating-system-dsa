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
        self.add_node(from_node)
        self.add_node(to_node)
        self.adjacency_List[from_node].append((to_node, weight))
        self.adjacency_List[to_node].append((from_node,weight))
    
    # Find shortest path using Dijkstra's algorithm:
    def dijkstra_Algorithm(self, start,end):
        priority_queue=[(0,start)]
        distances={node:float('inf') for node in self.adjacency_List}
        distances[start]=0
        pedecessors={node:None for node in self.adjacency_List}
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_node==end:
                break
            if current_distance>distances[current_node]:
                continue
            for neighbor, weight in self.adjacency_List[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    pedecessors[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        # Reconstruct the path:
        path=[]
        current=end
        while current:
            path.insert(0,current)
            current=pedecessors[current]
        if distances[end]==float('inf'):
            return float('inf'),[]
        return distances[end],path

graph = Graph()
graph.add_edge("A", "B", 4)
graph.add_edge("A", "C", 2)
graph.add_edge("B", "C", 1)
graph.add_edge("B", "D", 5)
graph.add_edge("C", "D", 8)
graph.add_edge("C", "E", 10)
graph.add_edge("D", "E", 2)
graph.add_edge("D", "Z", 6)
graph.add_edge("E", "Z", 3)
distance, path = graph.dijkstra_Algorithm("A", "Z")
print(f"Shortest distance: {distance}")
print(f"Path: {' -> '.join(path)}")
