import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt
import networkx as nx

class GraphUI:
    def __init__(self, root, graph):
        self.root = root
        self.graph = graph
        self.root.title("Graph Management UI")

        # Create buttons
        self.create_buttons()

    def create_buttons(self):
        # Add Device
        self.add_device_button = tk.Button(self.root, text="Add Device", command=self.add_device)
        self.add_device_button.grid(row=0, column=0, padx=10, pady=10)

        # Remove Device
        self.remove_device_button = tk.Button(self.root, text="Remove Device", command=self.remove_device)
        self.remove_device_button.grid(row=0, column=1, padx=10, pady=10)

        # Add Connection
        self.add_connection_button = tk.Button(self.root, text="Add Connection", command=self.add_connection)
        self.add_connection_button.grid(row=1, column=0, padx=10, pady=10)

        # Remove Connection
        self.remove_connection_button = tk.Button(self.root, text="Remove Connection", command=self.remove_connection)
        self.remove_connection_button.grid(row=1, column=1, padx=10, pady=10)

        # BFS
        self.bfs_button = tk.Button(self.root, text="BFS", command=self.bfs)
        self.bfs_button.grid(row=2, column=0, padx=10, pady=10)

        # DFS
        self.dfs_button = tk.Button(self.root, text="DFS", command=self.dfs)
        self.dfs_button.grid(row=2, column=1, padx=10, pady=10)

        # Dijkstra
        self.dijkstra_button = tk.Button(self.root, text="Dijkstra's Algorithm", command=self.dijkstra)
        self.dijkstra_button.grid(row=3, column=0, padx=10, pady=10)

        # Show Network Structure
        self.show_network_button = tk.Button(self.root, text="Show Network Structure", command=self.show_network_structure)
        self.show_network_button.grid(row=3, column=1, padx=10, pady=10)

        # Visualize Network
        self.visualize_button = tk.Button(self.root, text="Visualize Network", command=self.visualize_network)
        self.visualize_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def add_device(self):
        device = simpledialog.askstring("Input", "Enter the device name:")
        if device:
            self.graph.add_node(device)
            messagebox.showinfo("Success", f"Device '{device}' added.")

    def remove_device(self):
        device = simpledialog.askstring("Input", "Enter the device name to remove:")
        if device:
            self.graph.remove_node(device)
            messagebox.showinfo("Success", f"Device '{device}' removed.")

    def add_connection(self):
        from_device = simpledialog.askstring("Input", "Enter the first device:")
        to_device = simpledialog.askstring("Input", "Enter the second device:")
        weight = simpledialog.askfloat("Input", "Enter the connection weight:")

        if from_device and to_device and weight is not None:
            self.graph.add_edge(from_device, to_device, weight)
            messagebox.showinfo("Success", f"Connection added between '{from_device}' and '{to_device}' with weight {weight}.")

    def remove_connection(self):
        from_device = simpledialog.askstring("Input", "Enter the first device:")
        to_device = simpledialog.askstring("Input", "Enter the second device:")
        
        if from_device and to_device:
            self.graph.remove_edge(from_device, to_device)
            messagebox.showinfo("Success", f"Connection removed between '{from_device}' and '{to_device}'.")

    def bfs(self):
        start_device = simpledialog.askstring("Input", "Enter the starting device for BFS:")
        if start_device:
            reachable = self.graph.bfs(start_device)
            messagebox.showinfo("BFS Result", f"Devices reachable from '{start_device}': {reachable}")

    def dfs(self):
        start_device = simpledialog.askstring("Input", "Enter the starting device for DFS:")
        if start_device:
            reachable = self.graph.dfs(start_device)
            messagebox.showinfo("DFS Result", f"Devices connected to '{start_device}': {reachable}")

    def dijkstra(self):
        start_device = simpledialog.askstring("Input", "Enter the starting device:")
        end_device = simpledialog.askstring("Input", "Enter the target device:")

        if start_device and end_device:
            distance, path = self.graph.dijkstra_Algorithm(start_device, end_device)
            if distance == float('inf'):
                messagebox.showinfo("Dijkstra Result", f"No path exists between '{start_device}' and '{end_device}'.")
            else:
                messagebox.showinfo("Dijkstra Result", f"Shortest distance from '{start_device}' to '{end_device}': {distance}\nPath: {' -> '.join(path)}")

    def show_network_structure(self):
        structure = "\n".join([f"{node}: {edges}" for node, edges in self.graph.adjacency_List.items()])
        messagebox.showinfo("Network Structure", structure)

    def visualize_network(self):
        self.graph.visualize()

# Main part to start the application
if __name__ == "__main__":
    from DataStructures.Graph import Graph  # Assuming you already have the Graph class defined in another file named 'graph.py'

    # Create the graph object
    graph = Graph()

    # Initialize tkinter root window
    root = tk.Tk()

    # Create the UI
    app = GraphUI(root, graph)

    # Start the Tkinter event loop
    root.mainloop()
