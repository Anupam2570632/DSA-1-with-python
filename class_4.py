def linear_search(arr, target, index=0):
    # Base case: if index reaches the length of the array, target not found
    if index == len(arr):
        return -1  # Target not found

    # Base case: if the target is found
    if arr[index] == target:
        return index  # Return the index where target is found

    # Recursive case: call linear_search with the next index
    return linear_search(arr, target, index + 1)

# Example usage:
arr = [12, 34, 5, 23, 7, 6]
target = 23

result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
