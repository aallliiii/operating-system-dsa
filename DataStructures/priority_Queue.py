import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
    
    # Enqueue Function:
    def enqueue(self, item, priority):
            priority_int=int(priority)
            heapq.heappush(self._queue, (-priority_int, item))
            print(f"Enqueued: {item} with priority {priority_int}")
       

    # Dequeue function:
    def dequeue(self):
        if self._queue:
            priority,item=heapq.heappop(self._queue)
            return item,-priority
        else:
            return None,None
        
    # peek function:
    def peek(self):
        if self._queue:
            priority,item=self._queue[0]
            return item,-priority
        return None,None
    
    #Check Empty Queue:
    def is_empty(self):
        return len(self._queue) == 0
    
    def dequeue_all(self):
        tasks = []
        while not self.is_empty():
            task, priority = self.dequeue()
            tasks.append((task, priority))
        return tasks
        

# P_Q=PriorityQueue()
# P_Q.enqueue("TaskA", 3)
# P_Q.enqueue("TaskB", 1)
# P_Q.enqueue("TaskC", 2)
# item,priority=P_Q.dequeue()
# print(item,priority)  # Output: ('A', 3)
