import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextBrowser, QMessageBox
from OS_System import OS_System  # Import OS_System only

class OS_UI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.system = OS_System()  # OS_System object with Memory Manager, Task Scheduler, File System
        self.system.initialize_memory()

    def init_ui(self):
        self.setWindowTitle("Operating System Flow")
        self.setGeometry(100, 100, 600, 600)

        # Layout for UI components
        self.layout = QVBoxLayout()

        # Task Scheduling Section
        self.task_label = QLabel("Task Name:")
        self.layout.addWidget(self.task_label)
        self.task_input = QLineEdit()
        self.layout.addWidget(self.task_input)

        self.priority_label = QLabel("Task Priority (1-10):")
        self.layout.addWidget(self.priority_label)
        self.priority_input = QLineEdit()
        self.layout.addWidget(self.priority_input)

        self.schedule_button = QPushButton("Schedule Task")
        self.schedule_button.clicked.connect(self.schedule_task)
        self.layout.addWidget(self.schedule_button)

        # Memory Allocation Section
        self.allocate_button = QPushButton("Allocate Memory for Task")
        self.allocate_button.clicked.connect(self.allocate_memory)
        self.layout.addWidget(self.allocate_button)

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
        priority = self.priority_input.text()

        if not task_name or not priority:
            QMessageBox.warning(self, "Input Error", "Please enter both task name and priority.")
            return

        try:
            priority = int(priority)
            if priority < 1 or priority > 10:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Priority must be an integer between 1 and 10.")
            return

        self.system.schedule_task(priority, task_name)
        self.task_input.clear()
        self.priority_input.clear()

        # Update memory, task queue, and file system display
        self.update_display()

    def allocate_memory(self):
        task_name = self.task_input.text()
        if not task_name:
            QMessageBox.warning(self, "Input Error", "Please enter a task name to allocate memory.")
            return

        self.system.allocate_memory(task_name)
        self.update_display()

    def execute_task(self):
        self.system.execute_task()
        self.update_display()

    def update_display(self):
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
