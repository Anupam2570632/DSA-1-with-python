def InsertionSort(arr):
    for i in range(1, len(arr)-1):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
# example
arr = [3, -5, 1, -11, 3, -9, 23]
print(InsertionSort(arr))