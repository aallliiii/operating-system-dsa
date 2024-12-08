from DataStructures.priority_Queue import PriorityQueue
from DataStructures.linked_list import LinkedListMemoryManager

class ManageTasks:
    def __init__(self):
        self.tasks = {}
        self.priority_queue = PriorityQueue()
        self.memory_manager = LinkedListMemoryManager()
        self.memory_manager.initialize_Memory(500,100)
        

    def addTasksToQueue(self, item, priority):
        priority1=int(priority)
        print(type(priority1))
        self.priority_queue.enqueue(priority1, item)
        self.memory_manager.allocate(10)
    
    def Display_memory(self):
        return self.memory_manager.display_memory()

    def execute_tasks(self):
        executed_tasks = self.priority_queue.dequeue_all()
        print(executed_tasks)
        for tasks in executed_tasks:
            self.memory_manager.deallocate(10)
        return executed_tasks