import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
    
    # Enqueue Function:
    def enqueue(self, priority,item, file_name, path):
            priority_int=int(priority)
            task_name = item['task_name']
            category = item['category']
            heapq.heappush(self._queue, (-priority_int, task_name, category, file_name, path))
            # print(f"Enqueued: {item} with priority {priority_int}")
       

    # Dequeue function:
    def dequeue(self):
        if self._queue:
            priority,task_name, category,file_name, folder_name=heapq.heappop(self._queue)
            item = {
                'task_name': task_name,
                'category': category,
            }
            return item,-priority, file_name, folder_name
        else:
            return None,None,None,None
        
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
            task, priority, file_name, folder_name = self.dequeue()
            
            tasks.append((task, priority, file_name, folder_name))
        return tasks
        

# P_Q=PriorityQueue()
# P_Q.enqueue("TaskA", 3)
# P_Q.enqueue("TaskB", 1)
# P_Q.enqueue("TaskC", 2)
# item,priority=P_Q.dequeue()
# print(item,priority)  # Output: ('A', 3)
