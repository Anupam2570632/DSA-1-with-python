def MaxValue(arr, left, right):
    if(left == right):
        return  arr[left]
    
    mid = (left + right) // 2
    
    LM = MaxValue(arr, left, mid)
    RM = MaxValue(arr, mid + 1, right)
    
    return max(LM, RM)
    
# example
arr = [2, 6, 3, 18, 12, 21, 32, 174]

print(MaxValue(arr, 0, len(arr)-1))