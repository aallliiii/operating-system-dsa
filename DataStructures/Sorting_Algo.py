class SortingAlgorithm:
    @staticmethod
    def merge_sort(task_history, priority_list):
        if len(priority_list) > 1:
            mid = len(priority_list) // 2
            left_task_history = task_history[:mid]
            right_task_history = task_history[mid:]
            left_priority = priority_list[:mid]
            right_priority = priority_list[mid:]

            SortingAlgorithm.merge_sort(left_task_history, left_priority)
            SortingAlgorithm.merge_sort(right_task_history, right_priority)
            
            i = j = k = 0
            while i < len(left_priority) and j < len(right_priority):
                # Compare based on priority for descending order
                if left_priority[i] > right_priority[j]:  # Prioritize higher priority first
                    task_history[k] = left_task_history[i]
                    priority_list[k] = left_priority[i]
                    i += 1
                else:
                    task_history[k] = right_task_history[j]
                    priority_list[k] = right_priority[j]
                    j += 1
                k += 1

            # Handle any remaining elements in the left_half
            while i < len(left_priority):
                task_history[k] = left_task_history[i]
                priority_list[k] = left_priority[i]
                i += 1
                k += 1
        
            # Handle any remaining elements in the right_half
            while j < len(right_priority):
                task_history[k] = right_task_history[j]
                priority_list[k] = right_priority[j]
                j += 1
                k += 1

        return task_history, priority_list


