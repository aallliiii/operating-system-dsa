class SortingAlgorihtm:
    @staticmethod
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]
            SortingAlgorihtm.merge_sort(left_half)
            SortingAlgorihtm.merge_sort(right_half)
            i=j=k=0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k+=1
            while i<len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1
        
            while j<len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
        return arr
    
# arr=[1,4,3,9,55,67,99]
# print(SortingAlgorihtm.merge_sort(arr))