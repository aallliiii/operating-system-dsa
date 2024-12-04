from DataStructures.priority_Queue import PriorityQueue
from DataStructures.linked_list import LinkedListMemoryManager

class ManageTasks:
    def __init__(self):
        self.tasks = {}
        self.priority_queue = PriorityQueue()
        self.memory_manager = LinkedListMemoryManager()
        self.memory_manager.add_block(5000)
        

    def addTasksToQueue(self, item, priority):
        self.priority_queue.enqueue(priority, item)
        self.memory_manager.allocate(10)
    
    def display_memory(self):
        return self.memory_manager.display_memory()

    def execute_tasks(self):
        executed_tasks = self.priority_queue.dequeue_all()
        for tasks in executed_tasks:
            self.memory_manager.deallocate(10)
        return executed_tasks