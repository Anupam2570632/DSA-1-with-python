def Merge(arr1, arr2):
    
    i, j = 0, 0
    mergeArr=[]
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            mergeArr.append(arr1[i])
            i += 1
        else:
            mergeArr.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        mergeArr.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        mergeArr.append(arr2[j])
        j += 1
    
    return mergeArr

# example
arr1 = [-1, 1, 3, 6]
arr2 = [2, 4, 5]

print(Merge(arr1, arr2))