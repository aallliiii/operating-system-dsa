from DataStructures.priority_Queue import PriorityQueue
from DataStructures.linked_list import LinkedListMemoryManager

class ManageTasks:
    def __init__(self):
        self.tasks = {}
        self.priority_queue = PriorityQueue()
        self.memory_manager = LinkedListMemoryManager()

    def addTasksToQueue(self, item, priority):
        self.priority_queue.enqueue(priority, item)

    def execute_tasks(self):
        executed_tasks = self.priority_queue.dequeue_all()
        return executed_tasks