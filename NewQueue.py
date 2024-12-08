queue = []
front = - 1
rear = -1

def enq(value):
    global  front, rear, queue
    if front == -1:
        front = 0
    rear += 1
    
    queue.append(value)
def dequeue():
    global  front, rear, queue
    
    if front == -1 or front> rear:
        print("Queue is empty");
    else:
        print(f"dequeued: {queue[front]}")
        front += 1
   
    
def show():
    enq(10)
    enq(11)
    dequeue()
    
    print("Queue", queue[front:rear+1]);

show()