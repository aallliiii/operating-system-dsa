import sys
from manageTasks import ManageTasks
from DataStructures.BST import BinarySearchTree
from DataStructures.Graph import Graph
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel,
    QPushButton, QLineEdit, QListWidget, QTextEdit, QFormLayout, QComboBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class DataStructureApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

        # Data structures
        self.task_manager = ManageTasks()
        self.file_system = BinarySearchTree()
        self.network_graph = Graph()

    def init_ui(self):
        self.setWindowTitle("Data Structures Dashboard")
        self.setGeometry(0, 0, 1200, 800)  # Adjusted size for fullscreen
        self.showMaximized()  # Open in fullscreen

        # Styling
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2b2b2b; /* Dark grey background */
                color: #a4c639; /* Light green text */
            }
            QLabel {
                font-size: 18px;
                color: #a4c639;
            }
            QPushButton {
                background-color: #a4c639;
                color: #2b2b2b;
                font-size: 16px;
                padding: 8px 16px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #8bb630;
            }
            QLineEdit, QTextEdit, QListWidget, QComboBox {
                background-color: #3b3b3b;
                color: #a4c639;
                border: 1px solid #a4c639;
                border-radius: 5px;
            }
        """)

        # Layout
        central_widget = QWidget()
        main_layout = QVBoxLayout()

        # Add sections
        main_layout.addWidget(self.create_task_scheduler_section())
        main_layout.addWidget(self.create_file_system_section())
        main_layout.addWidget(self.create_graph_section())

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def create_task_scheduler_section(self):
        section = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Task Scheduler"))

        # Dropdown for task types
        self.task_dropdown = QComboBox()
        self.task_dropdown.addItems(["Select Task", "Send Email", "Upload File", "Run Backup", "Generate Report", "System Maintenance"])
        self.task_dropdown.currentIndexChanged.connect(self.dropdown_changed)

        self.task_list = QListWidget()
        self.add_task_btn = QPushButton("Add Task")
        self.execute_task_btn = QPushButton("Execute Task")

        task_form = QFormLayout()
        task_form.addRow("Task Type:", self.task_dropdown)

        layout.addLayout(task_form)
        layout.addWidget(self.task_list)
        layout.addWidget(self.add_task_btn)
        layout.addWidget(self.execute_task_btn)

        self.add_task_btn.clicked.connect(self.add_task)
        self.execute_task_btn.clicked.connect(self.execute_task)

        section.setLayout(layout)
        return section

    def create_file_system_section(self):
        section = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("File System"))
        self.file_output = QTextEdit()
        self.file_output.setReadOnly(True)
        self.file_input = QLineEdit()
        self.add_file_btn = QPushButton("Add File")
        self.view_files_btn = QPushButton("View All Files")

        file_form = QFormLayout()
        file_form.addRow("File Name:", self.file_input)

        layout.addLayout(file_form)
        layout.addWidget(self.file_output)
        layout.addWidget(self.add_file_btn)
        layout.addWidget(self.view_files_btn)

        self.add_file_btn.clicked.connect(self.add_file)
        self.view_files_btn.clicked.connect(self.view_files)

        section.setLayout(layout)
        return section

    def create_graph_section(self):
        section = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Networking (Graph)"))
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

        graph_form = QFormLayout()
        graph_form.addRow("Node:", self.node_input)
        graph_form.addRow("From Node:", self.edge_from_input)
        graph_form.addRow("To Node:", self.edge_to_input)
        graph_form.addRow("Weight:", self.edge_weight_input)
        graph_form.addRow("Start Node:", self.start_node_input)
        graph_form.addRow("End Node:", self.end_node_input)

        layout.addLayout(graph_form)
        layout.addWidget(self.graph_output)
        layout.addWidget(self.add_node_btn)
        layout.addWidget(self.add_edge_btn)
        layout.addWidget(self.shortest_path_btn)

        self.add_node_btn.clicked.connect(self.add_node)
        self.add_edge_btn.clicked.connect(self.add_edge)
        self.shortest_path_btn.clicked.connect(self.find_shortest_path)

        section.setLayout(layout)
        return section

    # Task Scheduler Functions
    def dropdown_changed(self):
        selected_task = self.task_dropdown.currentText()
        print(f"Selected Task: {selected_task}")  # Debugging line (optional)

    def add_task(self):
        task = self.task_dropdown.currentText()
        priorities = {
            "Send Email": 1,
            "Upload File": 2,
            "Run Backup": 3,
            "Generate Report": 4,
            "System Maintenance": 5
        }
        if task == "Select Task":
            self.task_list.addItem("Please select a valid task.")
        else:
            priority = priorities.get(task, 99)  # Default priority 99 if not listed
            self.task_manager.addTasksToQueue(task, priority)
            self.task_list.addItem(f"{task} (Priority: {priority})")
            self.task_dropdown.setCurrentIndex(0)  # Reset dropdown

    def execute_task(self):
        executed_tasks = self.task_manager.execute_tasks()
        if executed_tasks:
            for task, priority in executed_tasks:
                self.task_list.addItem(f"Executed: {task} (Priority: {priority})")
            self.task_list.addItem("All tasks executed.")
        else:
            self.task_list.addItem("No tasks to execute.")

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
