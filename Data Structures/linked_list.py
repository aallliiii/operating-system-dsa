class Node:
    def __init__(self,size,allocated=False):
        self.size = size
        self.allocated = allocated
        self.next=None

class LinkedListMemoryManager:
    def __init__(self):
        self.head = None
    
    # Add Block:
    def add_block(self, size):
        new_block = Node(size)
        if self.head is None:
            self.head = new_block
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_block
             
    # allocate:
    def allocate(self, size):
        current = self.head
        while current:
            if not current.allocated and current.size>= size:
                current.allocated = True
                current.size-=size
                return f"Allocated {size}MB."
            current = current.next
        return "No free block of that size available"
    
    # deallocate:
    def deallocate(self, size):
        current = self.head
        while current:
            if current.allocated :
                current.size+=size
                current.allocated = False
                return f"Deallocated {size}MB."
            current = current.next
        return "No block to deallocate"
    
    # Display Memory:
    def display_memory(self):
        result=[]
        current = self.head
        while current:
            state="Free" if current.allocated else "Free"
            result.append(f"[{current.size}MB - {state}]")
            current = current.next
        return " -> ".join(result)
    

# Initialize the memory manager
manager = LinkedListMemoryManager()

# Add memory blocks
manager.add_block(50)   # Add a 50MB block
manager.add_block(100)  # Add a 100MB block
manager.add_block(200)  # Add a 200MB block

# Display initial memory state
print("Initial Memory State:")
print(manager.display_memory())

# Allocate memory
print("\nAllocating 30MB:")
print(manager.allocate(30))
print(manager.display_memory())

# Allocate more memory
print("\nAllocating 120MB:")
print(manager.allocate(120))
print(manager.display_memory())

# Deallocate memory
print("\nDeallocating 120MB:")
print(manager.deallocate(120))
print(manager.display_memory())

# Attempt to allocate more than available
print("\nAllocating 300MB:")
print(manager.allocate(300))
print(manager.display_memory())


