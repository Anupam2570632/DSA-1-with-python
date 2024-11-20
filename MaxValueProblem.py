def MaxValue(arr, left, right):
    if(left == right):
        return  arr[left]
    
    mid = (left + right) // 2
    
    LM = MaxValue(arr, left, mid)
    RM = MaxValue(arr, mid + 1, right)
    
    if( LM > RM):
        return LM
    else:
        return RM
    
# example
arr = [2, 6, 3, 18, 12, 21, 32, 17]

print(MaxValue(arr, 0, len(arr)-1))