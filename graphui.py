import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget, QPushButton, QLineEdit, QLabel, QFormLayout, QInputDialog, QMessageBox
from PyQt5.QtCore import Qt
from DataStructures.Graph import Graph

# Define Graph class and methods here (same as before)

class GraphUI(QWidget):
    def __init__(self, graph):
        super().__init__()

        self.graph = graph  # The graph object
        self.init_ui()

    def init_ui(self):
        # Set the window title and size
        self.setWindowTitle('Graph Management')
        self.setGeometry(100, 100, 600, 400)

        # Create a vertical layout for the main window
        layout = QVBoxLayout()

        # Create a tab widget
        self.tabs = QTabWidget()

        # Create the tabs for different functionalities
        self.create_tabs()

        # Add the tabs widget to the layout
        layout.addWidget(self.tabs)

        # Set the layout to the main window
        self.setLayout(layout)

    def create_tabs(self):
        # Create a tab for Graph Operations
        graph_tab = QWidget()
        self.tabs.addTab(graph_tab, 'Graph Operations')

        # Create a layout for the Graph tab
        graph_layout = QVBoxLayout()

        # Create buttons for various graph operations
        self.add_device_button = QPushButton('Add Device')
        self.add_device_button.clicked.connect(self.add_device)

        self.remove_device_button = QPushButton('Remove Device')
        self.remove_device_button.clicked.connect(self.remove_device)

        self.add_connection_button = QPushButton('Add Connection')
        self.add_connection_button.clicked.connect(self.add_connection)

        self.remove_connection_button = QPushButton('Remove Connection')
        self.remove_connection_button.clicked.connect(self.remove_connection)

        self.bfs_button = QPushButton('BFS (Discover Reachable Devices)')
        self.bfs_button.clicked.connect(self.bfs)

        self.dfs_button = QPushButton('DFS (Explore Connections)')
        self.dfs_button.clicked.connect(self.dfs)

        self.dijkstra_button = QPushButton('Dijkstra (Shortest Path)')
        self.dijkstra_button.clicked.connect(self.dijkstra)

        self.visualize_button = QPushButton('Visualize Network')
        self.visualize_button.clicked.connect(self.visualize_network)

        # Add buttons to the Graph Layout
        graph_layout.addWidget(self.add_device_button)
        graph_layout.addWidget(self.remove_device_button)
        graph_layout.addWidget(self.add_connection_button)
        graph_layout.addWidget(self.remove_connection_button)
        graph_layout.addWidget(self.bfs_button)
        graph_layout.addWidget(self.dfs_button)
        graph_layout.addWidget(self.dijkstra_button)
        graph_layout.addWidget(self.visualize_button)

        # Set the layout for the Graph tab
        graph_tab.setLayout(graph_layout)

    def add_device(self):
        device, ok = QInputDialog.getText(self, 'Add Device', 'Enter the device name:')
        if ok and device:
            self.graph.add_node(device)
            QMessageBox.information(self, 'Success', f"Device '{device}' added.")

    def remove_device(self):
        device, ok = QInputDialog.getText(self, 'Remove Device', 'Enter the device name:')
        if ok and device:
            self.graph.remove_node(device)
            QMessageBox.information(self, 'Success', f"Device '{device}' removed.")

    def add_connection(self):
        from_device, ok1 = QInputDialog.getText(self, 'Add Connection', 'Enter the first device:')
        to_device, ok2 = QInputDialog.getText(self, 'Add Connection', 'Enter the second device:')
        if ok1 and ok2 and from_device and to_device:
            weight, ok3 = QInputDialog.getDouble(self, 'Connection Weight', 'Enter the connection weight:')
            if ok3:
                self.graph.add_edge(from_device, to_device, weight)
                QMessageBox.information(self, 'Success', f"Connection added between '{from_device}' and '{to_device}'.")

    def remove_connection(self):
        from_device, ok1 = QInputDialog.getText(self, 'Remove Connection', 'Enter the first device:')
        to_device, ok2 = QInputDialog.getText(self, 'Remove Connection', 'Enter the second device:')
        if ok1 and ok2 and from_device and to_device:
            self.graph.remove_edge(from_device, to_device)
            QMessageBox.information(self, 'Success', f"Connection removed between '{from_device}' and '{to_device}'.")

    def bfs(self):
        start_device, ok = QInputDialog.getText(self, 'BFS', 'Enter the starting device:')
        if ok and start_device:
            reachable = self.graph.bfs(start_device)
            QMessageBox.information(self, 'BFS Result', f"Devices reachable from '{start_device}': {reachable}")

    def dfs(self):
        start_device, ok = QInputDialog.getText(self, 'DFS', 'Enter the starting device:')
        if ok and start_device:
            reachable = self.graph.dfs(start_device)
            QMessageBox.information(self, 'DFS Result', f"Devices connected to '{start_device}': {reachable}")

    def dijkstra(self):
        start_device, ok1 = QInputDialog.getText(self, 'Dijkstra', 'Enter the starting device:')
        end_device, ok2 = QInputDialog.getText(self, 'Dijkstra', 'Enter the target device:')
        if ok1 and ok2 and start_device and end_device:
            distance, path = self.graph.dijkstra_Algorithm(start_device, end_device)
            if distance == float('inf'):
                QMessageBox.warning(self, 'Dijkstra Result', f"No path exists between '{start_device}' and '{end_device}'.")
            else:
                QMessageBox.information(self, 'Dijkstra Result', f"Shortest distance: {distance}\nPath: {' -> '.join(path)}")

    def visualize_network(self):
        self.graph.visualize()  # Calls the visualize method from the Graph class

# Main Application

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create an instance of the Graph class
    network_graph = Graph()

    # Create the GraphUI window
    graph_ui = GraphUI(network_graph)

    # Show the window
    graph_ui.show()

    # Run the application event loop
    sys.exit(app.exec_())
