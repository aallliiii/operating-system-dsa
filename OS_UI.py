import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextBrowser, QMessageBox, QComboBox, QProgressBar
)
from OS_System import OS_System  # Import the backend system

class OS_UI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.system = OS_System()  # OS_System object with Memory Manager, Task Scheduler, File System
        self.system.initialize_memory()

    def init_ui(self):
        self.setWindowTitle("Operating System Flow")
        self.setGeometry(100, 100, 600, 700)

        # Main Layout
        self.layout = QVBoxLayout()

        # Task Input Section
        self.task_label = QLabel("Task Name:")
        self.layout.addWidget(self.task_label)
        self.task_input = QLineEdit()
        self.layout.addWidget(self.task_input)

        self.task_type_label = QLabel("Select Task Type:")
        self.layout.addWidget(self.task_type_label)

        self.task_dropdown = QComboBox()  # Dropdown for task type
        self.task_dropdown.addItems(["File", "Folder", "Music", "Video"])  # Predefined task types
        self.layout.addWidget(self.task_dropdown)

        self.schedule_button = QPushButton("Schedule Task")
        self.schedule_button.clicked.connect(self.schedule_task)
        self.layout.addWidget(self.schedule_button)

        # Memory Usage Progress Bar
        self.memory_label = QLabel("Memory Usage:")
        self.layout.addWidget(self.memory_label)
        self.memory_progress = QProgressBar()
        self.memory_progress.setMaximum(500)  # Initial memory 500MB
        self.memory_progress.setValue(0)  # Start with 0 usage
        self.layout.addWidget(self.memory_progress)

        # Execute Task Section
        self.execute_button = QPushButton("Execute Task")
        self.execute_button.clicked.connect(self.execute_task)
        self.layout.addWidget(self.execute_button)

        # Display Section
        self.memory_display = QTextBrowser()
        self.layout.addWidget(self.memory_display)

        self.file_display = QTextBrowser()
        self.layout.addWidget(self.file_display)

        self.task_log_display = QTextBrowser()
        self.layout.addWidget(self.task_log_display)

        # Set Layout
        self.setLayout(self.layout)

    def schedule_task(self):
        task_name = self.task_input.text()
        task_type = self.task_dropdown.currentText()

        if not task_name:
            QMessageBox.warning(self, "Input Error", "Please enter a task name.")
            return

        # Task properties
        task_properties = {
            "File": (10, 1),
            "Folder": (20, 2),
            "Music": (5, 3),
            "Video": (30, 4),
        }

        memory_required, priority = task_properties[task_type]

        # Call backend to schedule task
        self.system.schedule_task(task_name, priority, memory_required)
        self.task_input.clear()

        # Update displays
        self.update_display()

    def execute_task(self):
        self.system.execute_task()
        self.update_display()

    def update_display(self):
        # Update memory usage progress bar
        used_memory = self.system.get_used_memory()
        self.memory_progress.setValue(used_memory)

        # Update memory display
        self.memory_display.setText(self.system.memory_manager.display_memory())

        # Update file system display
        self.file_display.setText(self.system.file_system.display())

        # Update task log
        self.task_log_display.setText("\n".join(self.system.task_log))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OS_UI()
    window.show()
    sys.exit(app.exec_())
