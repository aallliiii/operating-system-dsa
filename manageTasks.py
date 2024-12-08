from DataStructures.priority_Queue import PriorityQueue
from DataStructures.linked_list import LinkedListMemoryManager
from DataStructures.file_tree_system import FileSystem

class ManageTasks:
    def __init__(self):
        self.tasks = {}
        self.priority_queue = PriorityQueue()
        self.memory_manager = LinkedListMemoryManager()
        self.file_system = FileSystem()
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
    
    def create_file_or_folder(self, parent_name, name, is_folder=False):
        """ Create a file or folder in the file system """
        return self.file_system.add(parent_name, name, is_folder)

    def delete_file_or_folder(self, name):
        """ Delete a file or folder from the file system """
        return self.file_system.delete(name)

    def search_file(self, name):
        """ Search for a file or folder in the file system """
        return self.file_system.search(name)

    def display_file_system(self):
        """ Return the current file system structure as a string """
        return self.file_system.display()

    def update_file_or_folder(self, old_name, new_name, is_folder=False):
        """ Update file or folder name """
        return self.file_system.update(old_name, new_name, is_folder)