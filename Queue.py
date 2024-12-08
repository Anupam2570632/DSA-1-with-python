queue = []

# Enqueue (add element at the end of the queue)
def enqueue(queue, element):
    # Manually expand the list
    queue += [element]

# Dequeue (remove element from the front of the queue)
def dequeue(queue):
    if len(queue) == 0:
        return "Queue is empty"
    # Manually remove the first element
    first_element = queue[0]
    queue[:] = queue[1:]  # Update queue by slicing
    return first_element

# Test the manual queue operations
enqueue(queue, 1)  # Add 1 to the queue
enqueue(queue, 2)  # Add 2 to the queue
enqueue(queue, 3)  # Add 3 to the queue

print("Queue after enqueuing elements:", queue)

# Dequeue operations
print("Dequeued element:", dequeue(queue))
print("Queue after dequeuing an element:", queue)

print("Dequeued element:", dequeue(queue))
print("Queue after dequeuing an element:", queue)

print("Dequeued element:", dequeue(queue))
print("Queue after dequeuing an element:", queue)

# Attempt to dequeue from an empty queue
print("Dequeued element:", dequeue(queue))
