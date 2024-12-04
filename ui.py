import sys
from manageTasks import ManageTasks
from DataStructures.linked_list import LinkedListMemoryManager
from DataStructures.Graph import Graph
from DataStructures.BST import BinarySearchTree
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel,
    QPushButton, QLineEdit, QListWidget, QTextEdit, QFormLayout
)
from PyQt5.QtCore import Qt
class DataStructureApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

        # Data structures
        
        self.task_manager = ManageTasks()
        self.memory_manager = LinkedListMemoryManager()
        self.file_system = BinarySearchTree()
        self.network_graph = Graph()

    def init_ui(self):
        self.setWindowTitle("Data Structures UI")
        self.setGeometry(100, 100, 800, 600)

        # Layout
        central_widget = QWidget()
        main_layout = QVBoxLayout()

        # Add a task scheduler section
        self.task_list = QListWidget()
        self.task_input = QLineEdit()
        self.task_priority = QLineEdit()
        self.add_task_btn = QPushButton("Add Task")
        self.execute_task_btn = QPushButton("Execute Task")

        main_layout.addWidget(QLabel("Task Scheduler"))
        main_layout.addWidget(self.task_list)
        task_layout = QFormLayout()
        main_layout.addLayout(task_layout)

         # Task Scheduler Section
        main_layout.addWidget(QLabel("Task Scheduler"))
        main_layout.addWidget(self.task_list)
        task_layout = QFormLayout()
        task_layout.addRow("Task:", self.task_input)
        task_layout.addRow("Priority:", self.task_priority)
        main_layout.addLayout(task_layout)
        main_layout.addWidget(self.add_task_btn)
        main_layout.addWidget(self.execute_task_btn)

        self.add_task_btn.clicked.connect(self.add_task)
        self.execute_task_btn.clicked.connect(self.execute_task)

        # Memory Manager Section
        self.memory_output = QTextEdit()
        self.memory_output.setReadOnly(True)
        self.memory_input = QLineEdit()
        self.add_memory_btn = QPushButton("Add Memory Block")
        self.allocate_memory_btn = QPushButton("Allocate Memory")
        self.deallocate_memory_btn = QPushButton("Deallocate Memory")

        main_layout.addWidget(QLabel("Memory Manager"))
        main_layout.addWidget(self.memory_output)
        memory_layout = QFormLayout()
        memory_layout.addRow("Memory Size (MB):", self.memory_input)
        main_layout.addLayout(memory_layout)
        main_layout.addWidget(self.add_memory_btn)
        main_layout.addWidget(self.allocate_memory_btn)
        main_layout.addWidget(self.deallocate_memory_btn)

        self.add_memory_btn.clicked.connect(self.add_memory_block)
        self.allocate_memory_btn.clicked.connect(self.allocate_memory)
        self.deallocate_memory_btn.clicked.connect(self.deallocate_memory)

        # File System Section
        self.file_output = QTextEdit()
        self.file_output.setReadOnly(True)
        self.file_input = QLineEdit()
        self.add_file_btn = QPushButton("Add File")
        self.view_files_btn = QPushButton("View All Files")

        main_layout.addWidget(QLabel("File System"))
        main_layout.addWidget(self.file_output)
        file_layout = QFormLayout()
        file_layout.addRow("File Name:", self.file_input)
        main_layout.addLayout(file_layout)
        main_layout.addWidget(self.add_file_btn)
        main_layout.addWidget(self.view_files_btn)

        self.add_file_btn.clicked.connect(self.add_file)
        self.view_files_btn.clicked.connect(self.view_files)

        # Graph (Networking) Section
        self.graph_output = QTextEdit()
        self.graph_output.setReadOnly(True)
        self.node_input = QLineEdit()
        self.edge_from_input = QLineEdit()
        self.edge_to_input = QLineEdit()
        self.edge_weight_input = QLineEdit()
        self.start_node_input = QLineEdit()
        self.end_node_input = QLineEdit()
        self.add_node_btn = QPushButton("Add Node")
        self.add_edge_btn = QPushButton("Add Edge")
        self.shortest_path_btn = QPushButton("Find Shortest Path")

        main_layout.addWidget(QLabel("Networking (Graph)"))
        main_layout.addWidget(self.graph_output)
        graph_layout = QFormLayout()
        graph_layout.addRow("Node:", self.node_input)
        graph_layout.addRow("From Node:", self.edge_from_input)
        graph_layout.addRow("To Node:", self.edge_to_input)
        graph_layout.addRow("Weight:", self.edge_weight_input)
        graph_layout.addRow("Start Node:", self.start_node_input)
        graph_layout.addRow("End Node:", self.end_node_input)
        main_layout.addLayout(graph_layout)
        main_layout.addWidget(self.add_node_btn)
        main_layout.addWidget(self.add_edge_btn)
        main_layout.addWidget(self.shortest_path_btn)

        self.add_node_btn.clicked.connect(self.add_node)
        self.add_edge_btn.clicked.connect(self.add_edge)
        self.shortest_path_btn.clicked.connect(self.find_shortest_path)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    # Task Scheduler Functions
    def add_task(self):
        task = self.task_input.text()
        try:
            priority = int(self.task_priority.text())
            
            self.task_manager.addTasksToQueue(task, priority)
            self.task_list.addItem(f"{task} (Priority: {priority})")
            self.task_input.clear()
            self.task_priority.clear()
        except ValueError:
            self.task_list.addItem("Invalid priority value.")

    def execute_task(self):
        
        executed_tasks = self.task_manager.execute_tasks()
        if executed_tasks:
            for task, priority in executed_tasks:
                self.task_list.addItem(f"Executed: {task} (Priority: {priority})")
            self.task_list.addItem("All tasks executed.")  
        else:
            self.task_list.addItem("No tasks to execute.")


    # Memory Manager Functions
    def add_memory_block(self):
        try:
            size = int(self.memory_input.text())
            self.memory_manager.add_block(size)
            self.update_memory_output()
            self.memory_input.clear()
        except ValueError:
            self.memory_output.append("Invalid memory size.")

    def allocate_memory(self):
        
        try:
            size = int(self.memory_input.text())
            result = self.memory_manager.allocate(size)
            self.memory_output.append(result)
            self.update_memory_output()
            self.memory_input.clear()
        except ValueError:
            self.memory_output.append("Invalid memory size.")

    def deallocate_memory(self):
        result = self.memory_manager.deallocate()
        self.memory_output.append(result)
        self.update_memory_output()

    def update_memory_output(self):
        self.memory_output.setText(self.memory_manager.display_memory())

    # File System Functions
    def add_file(self):
        file_name = self.file_input.text()
        self.file_system.insert(file_name)
        self.file_output.append(f"Added file: {file_name}")
        self.file_input.clear()

    def view_files(self):
        files = self.file_system.inorder()
        self.file_output.setText("\n".join(files))

    # Graph Functions
    def add_node(self):
        node = self.node_input.text()
        self.network_graph.add_node(node)
        self.graph_output.append(f"Added node: {node}")
        self.node_input.clear()

    def add_edge(self):
        from_node = self.edge_from_input.text()
        to_node = self.edge_to_input.text()
        try:
            weight = int(self.edge_weight_input.text())
            self.network_graph.add_edge(from_node, to_node, weight)
            self.graph_output.append(f"Added edge: {from_node} -> {to_node} (Weight: {weight})")
            self.edge_from_input.clear()
            self.edge_to_input.clear()
            self.edge_weight_input.clear()
        except ValueError:
            self.graph_output.append("Invalid weight.")

    def find_shortest_path(self):
        start = self.start_node_input.text()
        end = self.end_node_input.text()
        distance, path = self.network_graph.dijkstra(start, end)
        if path:
            self.graph_output.append(f"Shortest path: {' -> '.join(path)} (Distance: {distance})")
        else:
            self.graph_output.append("No path found or invalid nodes.")


def main():
    app = QApplication(sys.argv)
    window = DataStructureApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
