from queue import Queue

def reverse_queue(q):
    stack = []

    # Dequeue all elements and push into stack
    while not q.empty():
        stack.append(q.get())

    # Pop from stack and enqueue back to queue
    while stack:
        q.put(stack.pop())

# Example usage
def main():
    q = Queue()
    for i in [10, 20, 30, 40, 50]:
        q.put(i)

    print("Original queue:")
    print(list(q.queue))

    reverse_queue(q)

    print("Reversed queue:")
    print(list(q.queue))

main()
