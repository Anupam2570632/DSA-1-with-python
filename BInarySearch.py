def BinarySearch(arr, start, end, target):
    
    if( start <= end ):
            # mid = (start + end) // 2 
            mid = start + (end - start) // 2
        
            if (arr[mid] == target):
                return 1
            
            elif arr[mid] > target:
                return BinarySearch(arr, start, mid - 1, target)
            
            elif arr[mid] < target:
                return BinarySearch(arr, mid + 1, end, target)
        
    return -1 
    
# example
arr = [2, 4, 6, 12, 25]
target = 22

if BinarySearch(arr, 0, len(arr)-1, target) == 1:
    print("Value Found on the array")
else:
    print("Value not found")