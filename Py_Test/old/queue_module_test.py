import queue

limit = 10

print("Queue")
q = queue.Queue()

for i in range(limit):
    q.put(i)

for i in range(limit):
    print(q.get(), end="→")


print("\nStack")
stack = queue.LifoQueue()

for i in range(limit):
    stack.put(i)

for i in range(limit):
    print(stack.get(), end="→")