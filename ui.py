import sys
from DataStructures import priority_Queue,Graph,BST,linked_list
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
        self.task_scheduler = priority_Queue()
        self.memory_manager = linked_list()
        self.file_system = BST()
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
        main_layout.addWidget(QFormLayout())