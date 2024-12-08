def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Step 1: Create buckets
    bucket_count = len(arr) 
    max_value = max(arr)
    buckets = [[] for _ in range(bucket_count)]

    # Step 2: Distribute elements into buckets
    for num in arr:
        index = int((num / max_value) * (bucket_count - 1))  
        buckets[index].append(num)

    # Step 3: Sort each bucket
    for bucket in buckets:
        bucket.sort()  

    # Step 4: Concatenate buckets into a single array
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

# Example usage
def show():
    arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.33, 0.83, 0.73, 0.12]
    print("Original array:", arr)
    sorted_arr = bucket_sort(arr)
    print("Sorted array:", sorted_arr)

show()