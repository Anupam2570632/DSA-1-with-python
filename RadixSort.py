def radix_sort(arr):
    if len(arr) == 0:
        return arr

    max_num = max(arr)
    exp = 1  

    # Perform sorting for each digit place
    while max_num // exp > 0:
        # Create buckets for each digit (0-9)
        buckets = [[] for _ in range(10)]

        # Distribute elements into buckets based on the current digit
        for num in arr:
            index = (num // exp) % 10
            buckets[index].append(num)

        # Flatten the buckets back into the array
        arr = []
        for bucket in buckets:
            arr.extend(bucket)

        # Move to the next significant digit
        exp *= 10

    return arr

# Example usage
def show():
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Original array:", arr)
    sorted_arr = radix_sort(arr)
    print("Sorted array:", sorted_arr)

show()