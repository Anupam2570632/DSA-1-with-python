def InsertionSort(arr):
    
    sortedArr = [arr[0]]
    
    for i in range(1, len(arr)):
        inserted = False
        
        for j in range(len(sortedArr)):
            if arr[i] < sortedArr[j]:
                sortedArr.insert(j, arr[i])
                inserted = True
                break

        if not inserted:
            sortedArr.append(arr[i])
            
            
    return sortedArr;
    
# example
arr = [3, -5, 6, -11, 3, 9, 23]
print(InsertionSort(arr))