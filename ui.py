import sys

from manageTasks import ManageTasks  # Assuming ManageTasks has task & memory logic
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel,
    QPushButton, QListWidget, QComboBox, QLineEdit, QTextEdit, QFormLayout, QProgressBar, QTabWidget, QHBoxLayout, QMessageBox, QInputDialog
)
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPalette, QColor, QFont
from DataStructures.Graph import Graph  # Assuming the Graph class is in graph.py



class OperatingSystemUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.task_manager = ManageTasks()  # Task and Memory logic
        self.init_ui()
        self.graph = Graph()  # Network Graph

    def init_ui(self):
        self.setWindowTitle("Operating System (OS)")
        self.setGeometry(100, 100, 1200, 800)
      

        # Styling
        self.setStyleSheet("""
            QMainWindow { background-color: #2b2b2b; color: #a4c639; }
            QLabel { font-size: 18px; color: #a4c639; }
            QPushButton { background-color: #a4c639; color: #2b2b2b; padding: 10px; border-radius: 5px; }
            QPushButton:hover { background-color: #8bb630; }
            QListWidget, QComboBox, QTextEdit, QLineEdit { background-color: #3b3b3b; color: #a4c639; border: 1px solid #a4c639; }
            QFrame { background-color: #555555; height: 2px; }
        """)

        # Central Widget and Tabs:
        central_widget = QWidget()
        layout = QVBoxLayout()
        self.tabs = QTabWidget()
        

        # Add Tabs
        self.tabs.addTab(self.create_task_manager_tab(), "Task Management")
        self.tabs.addTab(self.create_memory_manager_tab(), "Memory Management")
        self.tabs.addTab(self.create_file_system_tab(), "File Management")  # File Management Tab
        self.tabs.addTab(self.create_networking_tab(), "Networking")
        

        layout.addWidget(self.tabs)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    

    def create_task_manager_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        # Task Manager Section
        layout.addWidget(QLabel("Task Manager"))
        task_form = QFormLayout()

        # Task Name input field
        self.task_name_input = QLineEdit()
        self.task_name_input.setPlaceholderText("Enter Task Name")
        task_form.addRow("Task Name:", self.task_name_input)

        # Task Category dropdown
        self.task_category_dropdown = QComboBox()
        self.task_category_dropdown.addItems(["Select Category", "Add File", "Remove File", "Search File", "Add Folder"])
        self.task_category_dropdown.setStyleSheet("""
            QComboBox {
                color: #a4c639; /* Selected text color */
                background-color: #3b3b3b; /* Background color of the combobox */
                border: 1px solid #a4c639; /* Border color */
            }
            QComboBox QAbstractItemView {
                color: #a4c639; /* Item text color */
                background-color: #3b3b3b; /* Item background color */
            }
            QComboBox::drop-down {
                border: 1px solid #a4c639; /* Border for the dropdown arrow */
            }
        """)
        task_form.addRow("Select Task Category:", self.task_category_dropdown)



        #self.task_category_dropdown = QComboBox()
        #self.task_category_dropdown.addItems(["Select Category", "Add File", "Remove File", "Search File", "Add Folder"])
        #task_form.addRow("Select Task Category:", self.task_category_dropdown)

        # Additional Text Fields for File Name and Path
        self.file_name_input = QLineEdit()
        self.file_name_input.setPlaceholderText("Enter File/Folder Name")
        task_form.addRow("File/Folder Name:", self.file_name_input)

        self.file_path_input = QLineEdit()
        self.file_path_input.setPlaceholderText("Enter Parent Folder Name (e.g., root)")
        task_form.addRow("Parent Folder:", self.file_path_input)

        layout.addLayout(task_form)

        # Task List and Viewer
        self.task_list = QListWidget()
        layout.addWidget(QLabel("Scheduled Tasks:"))
        layout.addWidget(self.task_list)

        self.task_viewer = QListWidget()
        layout.addWidget(QLabel("Execution Tracker:"))
        layout.addWidget(self.task_viewer)


        # Buttons
        self.add_task_btn = QPushButton("Add Task")
        self.execute_task_btn = QPushButton("Execute Tasks")

        layout.addWidget(self.add_task_btn)
        layout.addWidget(self.execute_task_btn)

        # Connect Buttons
        self.add_task_btn.clicked.connect(self.add_task)
        self.execute_task_btn.clicked.connect(self.execute_tasks)

        tab.setLayout(layout)
        return tab


    def create_memory_manager_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        # Memory Manager Section
        layout.addWidget(QLabel("Memory Manager"))
        self.memory_progress = QProgressBar()
        self.memory_progress.setMaximum(1000)
        self.memory_progress.setValue(1000)  # Mock value
        layout.addWidget(self.memory_progress)

        self.memory_status = QTextEdit()
        self.memory_status.setReadOnly(True)
        self.update_memory_status()
        layout.addWidget(self.memory_status)

        tab.setLayout(layout)
        return tab

    def update_memory_status(self):
        # Updates the memory display and progress bar
        current = self.task_manager.memory_manager.head 
        used_memory = 0
        while current:
            if current.allocated:
                used_memory += current.size 
            current = current.next 
        
        total_memory = 1000  
        free_memory = total_memory - used_memory  
        self.memory_progress.setValue(free_memory)  

        # Update the memory block statuses
        memory_blocks = self.task_manager.memory_manager.display_memory()  
        self.memory_status.setText(f"Memory Blocks:\n{memory_blocks}")

    def add_task(self):
        task_name = self.task_name_input.text()
        category = self.task_category_dropdown.currentText()
        file_name = self.file_name_input.text()
        folder_name = self.file_path_input.text()
        

        priorities = {
            "Add File": 1,
            "Remove File": 2,
            "Search File": 3,
            "Add Folder": 4,
        }

        if task_name and category != "Select Category":
            try:
               
                name_and_category = {
                    "task_name": task_name,
                    "category": category
                }

                priority = int(priorities.get(category, 99))
                if category == 'Add File' or category == 'Add Folder':
                    self.task_manager.addTasksToQueue(name_and_category, priority, file_name, folder_name)
                elif category == 'Remove File' or category == 'Search File':
                    self.task_manager.addTasksToQueue(name_and_category, priority, file_name)
                else:
                    self.task_manager.addTasksToQueue(name_and_category, priority)
                self.task_list.addItem(f"Scheduled: {task_name} (Priority: {priority})")
                self.update_memory_status()
            except MemoryError as e:
                self.task_list.addItem(f"Error: {str(e)}")
        else:
            self.task_list.addItem("Invalid task name or category.")

        
        self.task_name_input.clear()
        self.file_name_input.clear()
        self.file_path_input.clear()
        self.task_category_dropdown.setCurrentIndex(0)

    def execute_tasks(self):
    

        executed_tasks = self.task_manager.execute_tasks()

        if not executed_tasks:
            self.task_viewer.addItem("No tasks to execute.")
            return

        
        self.task_viewer.addItem("Execution of tasks has begun")
        QTimer.singleShot(5000, lambda: self.execute_task_with_delay(executed_tasks))

    def execute_task_with_delay(self, tasks):
        
        if tasks:
            task, priority, file_name, folder_name = tasks.pop(0)

            if task['category'] == 'Add File':
                self.task_manager.create_file_or_folder(folder_name, file_name, is_folder=False)
                self.task_viewer.addItem(f"Executing: {task['task_name']} for adding file. (Priority: {priority})")
            elif task['category'] == 'Remove File':
                self.task_manager.delete_file_or_folder(file_name)
                self.task_viewer.addItem(f"Executing: {task['task_name']} for removing file (Priority: {priority})")
            elif task['category'] == 'Add Folder':
                self.task_manager.create_file_or_folder(folder_name, file_name, is_folder=True)
                self.task_viewer.addItem(f"Executing: {task['task_name']} for adding folder (Priority: {priority})")
            elif task['category'] == 'Search File':
                result = self.task_manager.search_file(file_name)
                self.task_viewer.addItem(f"Executing: {task['task_name']} for searching file (Priority: {priority})")
                self.task_viewer.addItem(result)

            self.update_memory_status()
            self.update_file_system_hierarchy()

            
            QTimer.singleShot(5000, lambda: self.execute_task_with_delay(tasks))
        else:
            self.task_viewer.addItem("All tasks executed. Memory reset.")
            self.update_memory_status()


    def create_file_system_tab(self):
        # File Management Tab
        tab = QWidget()
        layout = QVBoxLayout()

        # File Management Section
        layout.addWidget(QLabel("File Management"))

        # File System Hierarchy Display
        self.file_system_hierarchy = QTextEdit()
        self.file_system_hierarchy.setReadOnly(True)  # Make it read-only for display purposes
        layout.addWidget(QLabel("File System Hierarchy:"))
        layout.addWidget(self.file_system_hierarchy)

        # Update file system hierarchy initially
        self.update_file_system_hierarchy()

        tab.setLayout(layout)
        return tab


    def update_file_system_hierarchy(self):
        # Fetch and display the current file system structure
        hierarchy = self.task_manager.file_system.display()
        self.file_system_hierarchy.setText(hierarchy)

    def create_networking_tab(self):
        # Networking Tab
        tab = QWidget()
        layout = QVBoxLayout()

        # Main Split Layout (Window 1 and Window 2)
        split_layout = QHBoxLayout()

        # ---------------- Window 1 ----------------
        window1_layout = QVBoxLayout()
        #window1_layout.addWidget(QLabel("Window 1"))

        # Device Name Input
        self.device_name_input = QLineEdit()
        self.device_name_input.setPlaceholderText("Device Name (text box)")
        window1_layout.addWidget(self.device_name_input)

        # Combo Box for Task Selection
        self.device_action_dropdown = QComboBox()
        self.device_action_dropdown.addItems([
            "Add Device", "Remove Device"
        ])
        window1_layout.addWidget(self.device_action_dropdown)

        # Task Done Button
        self.task_done_btn_window1 = QPushButton("Task Done")
        window1_layout.addWidget(self.task_done_btn_window1)
        self.task_done_btn_window1.clicked.connect(self.handle_window1_action)

        # Add Window 1 to Split Layout
        split_layout.addLayout(window1_layout)

        # ---------------- Window 2 ----------------
        window2_layout = QVBoxLayout()
        #window2_layout.addWidget(QLabel("Window 2"))

        # Device A Input
        self.device_a_input = QLineEdit()
        self.device_a_input.setPlaceholderText("Device A")
        window2_layout.addWidget(self.device_a_input)

        # Device B Input
        self.device_b_input = QLineEdit()
        self.device_b_input.setPlaceholderText("Device B")
        window2_layout.addWidget(self.device_b_input)

        # Combo Box for Graph Actions
        self.graph_action_dropdown = QComboBox()
        self.graph_action_dropdown.addItems([
            "Add a Connection", "Remove a Connection", "BFS (Discover Reachable Devices)",
            "DFS (Explore Connections)", "Dijkstra's Algorithm (Shortest Path)"
        ])
        window2_layout.addWidget(self.graph_action_dropdown)

        # Task Done Button for Window 2
        self.task_done_btn_window2 = QPushButton("Task Done")
        window2_layout.addWidget(self.task_done_btn_window2)
        self.task_done_btn_window2.clicked.connect(self.handle_window2_action)

        # Add Window 2 to Split Layout
        split_layout.addLayout(window2_layout)

        # Add the split layout to the main layout
        layout.addLayout(split_layout)

        # Visualize Button
        self.visualize_btn = QPushButton("Visualize")
        layout.addWidget(self.visualize_btn)
        self.visualize_btn.clicked.connect(self.visualize_graph)

        tab.setLayout(layout)
        return tab

    def handle_window1_action(self):
        action = self.device_action_dropdown.currentText()
        device_name = self.device_name_input.text()

        if action == "Add Device":
            self.graph.add_node(device_name)
            QMessageBox.information(self, "Success", f"Device '{device_name}' added.")
        elif action == "Remove Device":
            self.graph.remove_node(device_name)
            QMessageBox.information(self, "Success", f"Device '{device_name}' removed.")
        else:
            QMessageBox.warning(self, "Error", "Invalid action selected!")

    def handle_window2_action(self):
        action = self.graph_action_dropdown.currentText()
        device_a = self.device_a_input.text()
        device_b = self.device_b_input.text()

        if action == "Add a Connection":
            weight, ok = QInputDialog.getDouble(self, "Connection Weight", "Enter weight:")
            if ok:
                self.graph.add_edge(device_a, device_b, weight)
                QMessageBox.information(self, "Success", f"Connection added between '{device_a}' and '{device_b}' with weight {weight}.")
        elif action == "Remove a Connection":
            self.graph.remove_edge(device_a, device_b)
            QMessageBox.information(self, "Success", f"Connection removed between '{device_a}' and '{device_b}'.")
        elif action == "BFS (Discover Reachable Devices)":
            result = self.graph.bfs(device_a)
            QMessageBox.information(self, "BFS Result", f"Reachable devices from '{device_a}': {result}")
        elif action == "DFS (Explore Connections)":
            result = self.graph.dfs(device_a)
            QMessageBox.information(self, "DFS Result", f"Connections explored from '{device_a}': {result}")
        elif action == "Dijkstra's Algorithm (Shortest Path)":
            distance, path = self.graph.dijkstra_Algorithm(device_a, device_b)
            if distance == float('inf'):
                QMessageBox.information(self, "Dijkstra Result", f"No path exists between '{device_a}' and '{device_b}'.")
            else:
                QMessageBox.information(self, "Dijkstra Result", f"Shortest path from '{device_a}' to '{device_b}': Distance {distance}, Path: {' -> '.join(path)}")
        else:
            QMessageBox.warning(self, "Error", "Invalid action selected!")

    def visualize_graph(self):
        self.graph.visualize()
        QMessageBox.information(self, "Visualize", "Graph visualization complete.")


def main():
    app = QApplication(sys.argv)
    window = OperatingSystemUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()