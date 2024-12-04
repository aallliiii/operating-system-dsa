import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
    
    # Enqueue Function:
    def enqueue(self, priority, item):
        heapq.heappush(self._queue, (-priority, item))

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
        

# P_Q=PriorityQueue()
# P_Q.enqueue("TaskA", 3)
# P_Q.enqueue("TaskB", 1)
# P_Q.enqueue("TaskC", 2)
# item,priority=P_Q.dequeue()
# print(item,priority)  # Output: ('A', 3)
