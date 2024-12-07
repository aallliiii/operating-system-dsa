from DataStructures.file_tree_system import FileSystem
from DataStructures.linked_list import LinkedListMemoryManager
from DataStructures.priority_Queue import PriorityQueue

class OS_System:
    def __init__(self):
        # Initialize File System, Memory Manager, and Task Scheduler
        self.file_system = FileSystem()
        self.memory_manager = LinkedListMemoryManager()
        self.task_scheduler = PriorityQueue()
        self.task_log = []  # To store executed tasks

    def initialize_memory(self):
        # Add some free memory blocks
        self.memory_manager.add_block(50)
        self.memory_manager.add_block(100)
        self.memory_manager.add_block(200)
        print("Memory initialized:")
        print(self.memory_manager.display_memory())

    #def schedule_task(self, task_name, priority):
    #    # Schedule task using priority queue
    #    self.task_scheduler.enqueue(task_name, priority)
    #    print(f"\nTask '{task_name}' with priority {priority} scheduled.")
    #    self.display_task_queue()

    def schedule_task(self, task_name, priority, memory_required):
        # Schedule task with given priority
        self.task_scheduler.enqueue(task_name, priority)
        print(f"Task '{task_name}' scheduled with priority {priority} and memory requirement {memory_required}MB.")
        self.memory_manager.add_block(memory_required)  # Add memory block for the task

    def get_used_memory(self):
    # Traverse the linked list to calculate used memory
        current = self.memory_manager.head
        used_memory = 0
        while current:
            if current.allocated:
                used_memory += current.size
            current = current.next
        return used_memory



    def allocate_memory(self, task_name):
        # Allocate memory for task from available memory blocks
        print(f"\nAllocating memory for task '{task_name}':")
        allocation_result = self.memory_manager.allocate(30)  # Example: allocate 30MB
        print(allocation_result)
        print(self.memory_manager.display_memory())

    def execute_task(self):
        # Execute the highest-priority task
        print("\nExecuting highest-priority task:")
        task, priority = self.task_scheduler.dequeue()
        if task:
            print(f"Task '{task}' with priority {priority} is executed.")
            # After execution, deallocate memory
            deallocation_result = self.memory_manager.deallocate(30)  # Example: deallocate 30MB
            print(deallocation_result)
            print(self.memory_manager.display_memory())
            # Add task to the file system
            self.file_system.add("root", task, False)  # Add as file under root folder
            print(f"Task '{task}' added to the file system.")
            self.task_log.append(task)
        else:
            print("No tasks to execute.")

    def display_task_queue(self):
        # Display current task queue
        tasks = []
        current = self.task_scheduler._queue
        for item in current:
            tasks.append(item[1])  # task name
        print("Current Task Queue:", tasks)

    def display_file_system(self):
        # Display current file system
        print("\nFile System:")
        print(self.file_system.display())

    def display_task_log(self):
        # Display executed tasks log
        print("\nExecuted Tasks Log:")
        print(self.task_log)

# Example Usage
#if __name__ == "__main__":
#    system = OS_System()
#
#    # Initialize memory
#    system.initialize_memory()
#
#    # Schedule tasks
#    system.schedule_task("TaskA", 3)
#    system.schedule_task("TaskB", 1)
#    system.schedule_task("TaskC", 2)
#
#    # Allocate memory
#    system.allocate_memory("TaskA")
#    system.allocate_memory("TaskB")
#
#    # Execute tasks
#    system.execute_task()
#    system.execute_task()
#
#    # Display file system and log
#    system.display_file_system()
#    system.display_task_log()
