import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Create an empty graph
G = nx.Graph()

def visualize_network():
    """Visualize the current network."""
    if len(G.nodes) == 0:
        print("The network is empty. Add devices to visualize.")
        return

    pos = nx.spring_layout(G)  # Generate positions for nodes
    plt.figure(figsize=(8, 6))  # Set the figure size
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color='lightblue',
        edge_color='gray',
        node_size=2000,
        font_size=10,
        font_weight='bold',
    )
    # Draw edge labels for weights
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    plt.title("Network Graph Visualization")
    plt.show()


def add_device():
    """Add a new device (node) to the network."""
    device = input("Enter the name of the device to add: ").strip()
    if device in G.nodes:
        print(f"Device '{device}' already exists in the network.")
    else:
        G.add_node(device)
        print(f"Device '{device}' added to the network.")


def remove_device():
    """Remove a device (node) from the network."""
    device = input("Enter the name of the device to remove: ").strip()
    if device not in G.nodes:
        print(f"Device '{device}' does not exist in the network.")
    else:
        G.remove_node(device)
        print(f"Device '{device}' removed from the network.")


def add_connection():
    """Add a connection (edge) between two devices."""
    device1 = input("Enter the first device: ").strip()
    device2 = input("Enter the second device: ").strip()
    if device1 not in G.nodes or device2 not in G.nodes:
        print("Both devices must exist in the network. Add them first.")
        return
    try:
        weight = float(input("Enter the weight of the connection (e.g., bandwidth/latency): "))
        G.add_edge(device1, device2, weight=weight)
        print(f"Connection added between '{device1}' and '{device2}' with weight {weight}.")
    except ValueError:
        print("Invalid weight. Please enter a number.")


def remove_connection():
    """Remove a connection (edge) between two devices."""
    device1 = input("Enter the first device: ").strip()
    device2 = input("Enter the second device: ").strip()
    if not G.has_edge(device1, device2):
        print(f"No connection exists between '{device1}' and '{device2}'.")
    else:
        G.remove_edge(device1, device2)
        print(f"Connection removed between '{device1}' and '{device2}'.")


def bfs():
    """Perform BFS to discover reachable devices from a starting device."""
    start = input("Enter the starting device for BFS: ").strip()
    if start not in G.nodes:
        print(f"Device '{start}' does not exist in the network.")
        return

    visited = set()
    queue = deque([start])
    reachable_devices = []

    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.add(current)
            reachable_devices.append(current)
            for neighbor in G.neighbors(current):
                if neighbor not in visited:
                    queue.append(neighbor)

    print(f"Devices reachable from '{start}': {reachable_devices}")


def dfs():
    """Perform DFS to explore connections from a starting device."""
    start = input("Enter the starting device for DFS: ").strip()
    if start not in G.nodes:
        print(f"Device '{start}' does not exist in the network.")
        return

    def dfs_recursive(node, visited):
        visited.add(node)
        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                dfs_recursive(neighbor, visited)

    visited = set()
    dfs_recursive(start, visited)
    print(f"Devices connected to '{start}': {list(visited)}")


def dijkstra():
    """Find shortest paths from a starting device using Dijkstra's algorithm."""
    start = input("Enter the starting device for Dijkstra's algorithm: ").strip()
    if start not in G.nodes:
        print(f"Device '{start}' does not exist in the network.")
        return

    distances = nx.single_source_dijkstra_path_length(G, source=start, weight='weight')
    print(f"Shortest paths from '{start}':")
    for node, distance in distances.items():
        print(f"  {node}: {distance}")


def display_menu():
    """Display the menu options."""
    print("\nNetwork Management Menu")
    print("1. Add a Device")
    print("2. Remove a Device")
    print("3. Add a Connection")
    print("4. Remove a Connection")
    print("5. Visualize Network")
    print("6. BFS (Breadth-First Search)")
    print("7. DFS (Depth-First Search)")
    print("8. Dijkstra's Algorithm (Shortest Path)")
    print("9. Exit")


def main():
    """Main function to run the menu-driven program."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ").strip()
        if choice == "1":
            add_device()
        elif choice == "2":
            remove_device()
        elif choice == "3":
            add_connection()
        elif choice == "4":
            remove_connection()
        elif choice == "5":
            visualize_network()
        elif choice == "6":
            bfs()
        elif choice == "7":
            dfs()
        elif choice == "8":
            dijkstra()
        elif choice == "9":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


# Run the program
if __name__ == "__main__":
    main()
