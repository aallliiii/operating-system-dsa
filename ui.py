import sys
from manageTasks import ManageTasks  # Assuming ManageTasks has task & memory logic
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel,
    QPushButton, QListWidget, QComboBox, QLineEdit, QTextEdit, QFormLayout, QProgressBar, QTabWidget
)
from PyQt5.QtCore import QTimer


class OperatingSystemUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.task_manager = ManageTasks()  # Task and Memory logic
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Operating System Demo")
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

        # Central Widget and Tabs
        central_widget = QWidget()
        layout = QVBoxLayout()
        self.tabs = QTabWidget()

        # Add Tabs
        self.tabs.addTab(self.create_task_manager_tab(), "Task Management")
        self.tabs.addTab(self.create_memory_manager_tab(), "Memory Management")
        self.tabs.addTab(self.create_file_system_tab(), "File Management")  # File Management Tab
        

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
        self.task_category_dropdown.addItems(["Select Category", "Email", "File Upload", "Backup", "Generate Report", "System Maintenance"])

        task_form.addRow("Select Task Category:", self.task_category_dropdown)
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
        self.memory_progress.setMaximum(500)
        self.memory_progress.setValue(500)  # Mock value
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
        
        total_memory = 500  
        free_memory = total_memory - used_memory  
        self.memory_progress.setValue(free_memory)  

        # Update the memory block statuses
        memory_blocks = self.task_manager.memory_manager.display_memory()  
        self.memory_status.setText(f"Memory Blocks:\n{memory_blocks}")

    def add_task(self):
        task_name = self.task_name_input.text()
        category = self.task_category_dropdown.currentText()

        priorities = {
            "Email": 1,
            "File Upload": 2,
            "Backup": 3,
            "Generate Report": 4,
            "System Maintenance": 5
        }

        if task_name and category != "Select Category":
            try:
                # Use the selected category priority
                priority = int(priorities.get(category, 99))
                self.task_manager.addTasksToQueue(task_name, priority)
                self.task_list.addItem(f"Scheduled: {task_name} (Priority: {priority})")
                self.update_memory_status()
            except MemoryError as e:
                self.task_list.addItem(f"Error: {str(e)}")
        else:
            self.task_list.addItem("Invalid task name or category.")

        # Clear the input fields after adding
        self.task_name_input.clear()
        self.task_category_dropdown.setCurrentIndex(0)

    def execute_tasks(self):
        # Executes tasks with a 5-second delay:
        executed_tasks = self.task_manager.execute_tasks()
        if not executed_tasks:
            self.task_viewer.addItem("No tasks to execute.")
            return

        self.execute_task_with_delay(executed_tasks)

    def execute_task_with_delay(self, tasks):
        # Executes tasks one by one with a 5-second delay:
        if tasks:
            task, priority = tasks.pop(0)
            self.task_viewer.addItem(f"Executing: {task} (Priority: {priority})")
            self.update_memory_status()

            # Delay for 5 seconds before executing the next task
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

        # Form for File Management Actions
        file_form = QFormLayout()

        # Dropdown for File Actions
        self.file_action_dropdown = QComboBox()
        self.file_action_dropdown.addItems(["Select Action", "Add File", "Add Folder", "Remove File", "Remove Folder"])
        file_form.addRow("Select Action:", self.file_action_dropdown)

        # Name input field for file/folder
        self.file_name_input = QLineEdit()
        self.file_name_input.setPlaceholderText("Enter file/folder name")
        file_form.addRow("Name:", self.file_name_input)

        # Path input field for file/folder
        self.file_path_input = QLineEdit()
        self.file_path_input.setPlaceholderText("Enter parent path (e.g., root)")
        file_form.addRow("Path:", self.file_path_input)

        layout.addLayout(file_form)

        # Button to perform the selected action
        self.perform_action_btn = QPushButton("Perform Action")
        layout.addWidget(self.perform_action_btn)

        # File System Hierarchy Display
        self.file_system_hierarchy = QTextEdit()
        self.file_system_hierarchy.setReadOnly(True)
        layout.addWidget(QLabel("File System Hierarchy:"))
        layout.addWidget(self.file_system_hierarchy)

        # Connect button click to the action handler
        self.perform_action_btn.clicked.connect(self.file_management_action)

        tab.setLayout(layout)
        return tab

    def file_management_action(self):
        # Get values from input fields
        action = self.file_action_dropdown.currentText()
        name = self.file_name_input.text()
        path = self.file_path_input.text()

        if action == "Add File":
            # Call method to add file
            result = self.task_manager.create_file_or_folder(path, name, is_folder=False)
        elif action == "Add Folder":
            # Call method to add folder
            result = self.task_manager.create_file_or_folder(path, name, is_folder=True)
        elif action == "Remove File":
            # Call method to remove file
            result = self.task_manager.delete_file_or_folder(name, is_folder=False)
        elif action == "Remove Folder":
            # Call method to remove folder
            result = self.task_manager.delete_file_or_folder(name, is_folder=True)
        else:
            result = "Invalid action selected!"

        # Display result and update file system hierarchy
        self.file_system_hierarchy.setText(result)
        self.update_file_system_hierarchy()

    def update_file_system_hierarchy(self):
        # Fetch and display the current file system structure
        hierarchy = self.task_manager.file_system.display()
        self.file_system_hierarchy.setText(hierarchy)


def main():
    app = QApplication(sys.argv)
    window = OperatingSystemUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()