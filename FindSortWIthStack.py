def sort(arr):
    stack = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i > j and arr[i] < arr[j]:
                stack.append(arr[j])
            else:
                return 0
    
def show():
    arr = [12, 8, 6, 11, 88]
    sort(arr)
    print(arr)

show()