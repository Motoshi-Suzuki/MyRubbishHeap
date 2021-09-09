
data_limit = 6
queue = [0] * data_limit
head = 0
tail = 0

def enqueue(data):
    global tail
    
    next = (tail + 1) % data_limit
    print("next:", next)

    if next == head:
        print("You can't enqueue more data")
    else:
        queue[tail] = data
        tail = next
        print("Data", data, "has enqueued")

def dequeue():
    global head

    if head == tail:
        print("No queued data")
        return None
    else:
        dequeued_data = queue[head]
        head = (head + 1) % data_limit
        print("head:", head)
        return dequeued_data

for i in range(data_limit):
    enqueue(i)

for i in range(data_limit):
    dequeued_data = dequeue()
    print("Dequeued data:", dequeued_data)