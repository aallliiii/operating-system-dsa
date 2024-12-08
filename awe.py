import sys
from manageTasks import ManageTasks
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel,
    QPushButton, QLineEdit, QListWidget, QFormLayout, QComboBox, QTextEdit, QFrame, QTabWidget
)
from PyQt5.QtCore import QTimer, Qt


class DataStructureApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.task_manager = ManageTasks()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Operating System (OS)")

        # Full Screen Size:
        self.setGeometry(0, 0, 1200, 800)  
        self.showMaximized()

        # Styling applying Here:
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2b2b2b; /* Dark grey background */
                color: #a4c639; /* Light green text */
            }
            QLabel {
                font-size: 20px;
                color: #a4c639;
                padding: 10px 0;
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
            QLineEdit, QComboBox, QListWidget, QTextEdit {
                background-color: #3b3b3b;
                color: #a4c639;
                border: 1px solid #a4c639;
                border-radius: 5px;
            }
            QFrame {
                background-color: #555555;
                height: 2px;
            }
        """)
        tabs=QTabWidget

        # Central Layout
        central_widget = QWidget()
        main_layout = QVBoxLayout()

        # tabs=QTabWidget()
        # tabs.addTab(self.create_task_manager_section(), "Task Manager & Memory Manager")
        # tabs.addTab(self.create_file_system_section(), "File System")

        # Add Task Manager and Memory Manager Sections
        main_layout.addWidget(self.create_task_manager_section())
        main_layout.addWidget(self.create_divider())
        main_layout.addWidget(self.create_memory_manager_section())

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def create_divider(self):

        # Creates a divider for visual separation:
        divider = QFrame()
        divider.setFrameShape(QFrame.HLine)
        divider.setFrameShadow(QFrame.Sunken)
        divider.setStyleSheet("background-color: #73e617;")
        return divider

    def create_task_manager_section(self):

        # Creates the Task Manager section:
        section = QWidget()
        layout = QVBoxLayout()

        # Task Input and Category
        layout.addWidget(QLabel("Task Manager"))

        self.task_name_input = QLineEdit()
        self.task_name_input.setPlaceholderText("Enter Task Name")

        self.task_category_dropdown = QComboBox()
        self.task_category_dropdown.addItems([
            "Select Category", "Email", "File Upload", "Backup", "Generate Report", "System Maintenance"
        ])

        self.add_task_btn = QPushButton("Add Task")
        self.execute_task_btn = QPushButton("Execute Tasks")

        task_form = QFormLayout()
        task_form.addRow("Task Name:", self.task_name_input)
        task_form.addRow("Task Category:", self.task_category_dropdown)

        # Task Viewer
        self.task_list = QListWidget()
        self.task_viewer = QListWidget()

        layout.addLayout(task_form)
        layout.addWidget(QLabel("Execution Tracker"))
        layout.addWidget(self.task_viewer)
        layout.addWidget(QLabel("Task Scheduler"))
        layout.addWidget(self.task_list)
        layout.addWidget(self.add_task_btn)
        layout.addWidget(self.execute_task_btn)

        # Connect Buttons
        self.add_task_btn.clicked.connect(self.add_task)
        self.execute_task_btn.clicked.connect(self.execute_tasks)
        

        section.setLayout(layout)
        return section

    def create_memory_manager_section(self):
        # Creates the Memory Manager section:
        section = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Memory Manager"))
        self.memory_output = QTextEdit()
        self.memory_output.setReadOnly(True)
        self.update_memory_output()

        layout.addWidget(self.memory_output)
        section.setLayout(layout)
        return section

    def update_memory_output(self):
        # Update memory display using ManageTasks logic:
        memory_state = self.task_manager.Display_memory()
        self.memory_output.setText(f"Memory Blocks:\n{memory_state}")

    def add_task(self):
        # Adds a task to the task queue:
        task_name = self.task_name_input.text()
        category = self.task_category_dropdown.currentText()

        priorities = {
            "Email": 1,
            "File Upload": 2,
            "Backup": 3,
            "Generate Report": 4,
            "System Maintenance": 5
        }

        if not task_name or category == "Select Category":
            self.task_list.addItem("Invalid task name or category.")
        else:
            priority = int(priorities.get(category, 99))
            try:
                # print(task_name,priority)
                self.task_manager.addTasksToQueue(task_name, priority)
                self.task_list.addItem(f"{task_name} ({category}, Priority: {priority})")
                self.update_memory_output()
            except MemoryError as e:
                self.task_list.addItem(str(e))

            self.task_name_input.clear()
            self.task_category_dropdown.setCurrentIndex(0)

    def execute_tasks(self):

        # Executes tasks with a 5-second delay:
        executed_tasks = self.task_manager.execute_tasks()
        if not executed_tasks:
            self.task_viewer.addItem("No tasks to execute.")
            return
        
        # Execute the Tasks with 5 seconds delay:
        self.execute_task_with_delay(executed_tasks)

    def execute_task_with_delay(self, tasks):
        # Executes tasks with a 5-second delay:
        if tasks:
            task, priority = tasks.pop(0)
            self.task_viewer.addItem(f"Executing: {task} (Priority: {priority})")
            self.update_memory_output()

            # Delay for 5 seconds before executing the next task
            QTimer.singleShot(5000, lambda: self.execute_task_with_delay(tasks))  
        else:
            self.task_viewer.addItem("All tasks executed. Memory updated.")
            self.update_memory_output()

    def create_file_system_section(self):
        """Creates the File System section."""
        section = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("File System"))

        self.file_input = QLineEdit()
        self.file_input.setPlaceholderText("Enter File Name")

        self.add_file_btn = QPushButton("Add File")
        self.view_files_btn = QPushButton("View All Files")

        self.file_output = QTextEdit()
        self.file_output.setReadOnly(True)

        file_form = QFormLayout()
        file_form.addRow("File Name:", self.file_input)

        layout.addLayout(file_form)
        layout.addWidget(self.file_output)
        layout.addWidget(self.add_file_btn)
        layout.addWidget(self.view_files_btn)

        # Connect Buttons
        self.add_file_btn.clicked.connect(self.add_file)
        self.view_files_btn.clicked.connect(self.view_files)

        section.setLayout(layout)
        return section
    
    def add_file(self):
        """Adds a file to the file system."""
        file_name = self.file_input.text()

        if file_name:
            self.task_manager.file_system.insert(file_name)  # Assuming `file_system` is initialized in ManageTasks
            self.file_output.append(f"Added file: {file_name}")
            self.file_input.clear()
        else:
            self.file_output.append("Please enter a valid file name.")

    def view_files(self):
        """Displays all files in the system."""
        files = self.task_manager.file_system.inorder()  # Assuming `file_system` is initialized in ManageTasks
        if files:
            self.file_output.setText("\n".join(files))
        else:
            self.file_output.setText("No files in the system.")


def main():
    app = QApplication(sys.argv)
    window = DataStructureApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()