import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.adjacency_List = {}
    
    # Add a node to the graph
    def add_node(self, node):
        if node not in self.adjacency_List:
            self.adjacency_List[node] = []

    # Add a weighted edge between two nodes
    def add_edge(self, from_node, to_node, weight):
        self.add_node(from_node)
        self.add_node(to_node)
        self.adjacency_List[from_node].append((to_node, weight))
        self.adjacency_List[to_node].append((from_node, weight))

    # Remove a node from the graph
    def remove_node(self, node):
        if node in self.adjacency_List:
            for neighbor, _ in self.adjacency_List[node]:
                self.adjacency_List[neighbor] = [
                    (n, w) for n, w in self.adjacency_List[neighbor] if n != node
                ]
            del self.adjacency_List[node]

    # Remove an edge between two nodes
    def remove_edge(self, from_node, to_node):
        if from_node in self.adjacency_List:
            self.adjacency_List[from_node] = [
                (n, w) for n, w in self.adjacency_List[from_node] if n != to_node
            ]
        if to_node in self.adjacency_List:
            self.adjacency_List[to_node] = [
                (n, w) for n, w in self.adjacency_List[to_node] if n != from_node
            ]

    # BFS traversal
    def bfs(self, start):
        visited = set()
        queue = [start]
        reachable = []

        while queue:
            current = queue.pop(0)
            if current not in visited:
                visited.add(current)
                reachable.append(current)
                for neighbor, _ in self.adjacency_List.get(current, []):
                    if neighbor not in visited:
                        queue.append(neighbor)

        return reachable

    # DFS traversal
    def dfs(self, start):
        visited = set()
        stack = [start]
        reachable = []

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                reachable.append(current)
                for neighbor, _ in self.adjacency_List.get(current, []):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return reachable

    # Dijkstra's algorithm
    def dijkstra_Algorithm(self, start, end):
        import heapq

        priority_queue = [(0, start)]
        distances = {node: float('inf') for node in self.adjacency_List}
        distances[start] = 0
        predecessors = {node: None for node in self.adjacency_List}

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_node == end:
                break
            if current_distance > distances[current_node]:
                continue
            for neighbor, weight in self.adjacency_List[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        # Reconstruct the path
        path = []
        current = end
        while current:
            path.insert(0, current)
            current = predecessors[current]
        if distances[end] == float('inf'):
            return float('inf'), []
        return distances[end], path

    # Visualize the graph using Matplotlib
    def visualize(self):
        import networkx as nx

        G = nx.Graph()
        for node, neighbors in self.adjacency_List.items():
            for neighbor, weight in neighbors:
                G.add_edge(node, neighbor, weight=weight)

        pos = nx.spring_layout(G)  # Layout for graph visualization
        plt.figure(figsize=(8, 6))

        # Draw nodes and edges
        nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold', node_size=2000)

        # Draw edge labels (weights)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.title("Network Structure")
        plt.show()

# Interactive Network Management
def display_menu():
    print("\nNetwork Management Menu")
    print("1. Add a Device")
    print("2. Remove a Device")
    print("3. Add a Connection")
    print("4. Remove a Connection")
    print("5. BFS (Discover Reachable Devices)")
    print("6. DFS (Explore Connections)")
    print("7. Dijkstra's Algorithm (Shortest Path)")
    print("8. Show Network Structure")
    print("9. Visualize Network")
    print("10. Exit")

def main():
    network = Graph()

    while True:
        display_menu()
        choice = input("Enter your choice (1-10): ").strip()

        if choice == "1":
            node = input("Enter the name of the device to add: ").strip()
            network.add_node(node)
            print(f"Device '{node}' added to the network.")

        elif choice == "2":
            node = input("Enter the name of the device to remove: ").strip()
            network.remove_node(node)
            print(f"Device '{node}' removed from the network.")

        elif choice == "3":
            from_node = input("Enter the first device: ").strip()
            to_node = input("Enter the second device: ").strip()
            try:
                weight = float(input("Enter the weight of the connection: "))
                network.add_edge(from_node, to_node, weight)
                print(f"Connection added between '{from_node}' and '{to_node}' with weight {weight}.")
            except ValueError:
                print("Invalid weight. Please enter a number.")

        elif choice == "4":
            from_node = input("Enter the first device: ").strip()
            to_node = input("Enter the second device: ").strip()
            network.remove_edge(from_node, to_node)
            print(f"Connection removed between '{from_node}' and '{to_node}'.")

        elif choice == "5":
            start = input("Enter the starting device for BFS: ").strip()
            if start not in network.adjacency_List:
                print(f"Device '{start}' does not exist in the network.")
            else:
                reachable = network.bfs(start)
                print(f"Devices reachable from '{start}': {reachable}")

        elif choice == "6":
            start = input("Enter the starting device for DFS: ").strip()
            if start not in network.adjacency_List:
                print(f"Device '{start}' does not exist in the network.")
            else:
                reachable = network.dfs(start)
                print(f"Devices connected to '{start}': {reachable}")

        elif choice == "7":
            start = input("Enter the starting device: ").strip()
            end = input("Enter the target device: ").strip()
            if start not in network.adjacency_List or end not in network.adjacency_List:
                print("Both devices must exist in the network.")
            else:
                distance, path = network.dijkstra_Algorithm(start, end)
                if distance == float('inf'):
                    print(f"No path exists between '{start}' and '{end}'.")
                else:
                    print(f"Shortest distance from '{start}' to '{end}': {distance}")
                    print(f"Path: {' -> '.join(path)}")

        elif choice == "8":
            print("\nNetwork Structure:")
            for node, edges in network.adjacency_List.items():
                print(f"{node}: {edges}")

        elif choice == "9":
            network.visualize()

        elif choice == "10":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 10.")

# Run the program
if __name__ == "__main__":
    main()
