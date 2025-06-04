# Here’s a complete explanation of the Queue data structure along with an implementation using an array in Python, covering:

# Operation	Description
# enqueue	Add element at the rear
# dequeue	Remove element from the front
# get_front	Return front element
# get_rear	Return rear element
# is_empty	Check if queue is empty
# is_full	Check if queue is full (in fixed size)

# 🔷 What is a Queue?
# A Queue is a linear data structure that follows the FIFO principle:

# First In First Out – The first element inserted is the first to be removed.

#Linear Queue

class LinearQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1

    def is_empty(self):
        return self.front > self.rear

    def is_full(self):
        return self.rear == self.capacity - 1

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full")
            return
        self.rear += 1
        self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        removed = self.queue[self.front]
        self.queue[self.front] = None  # Optional clear
        self.front += 1
        return removed

    def get_front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[self.front]

    def get_rear(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[self.rear]

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue elements:", end=' ')
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=' ')
            print()

def main():
    q = LinearQueue(5)

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)

    q.display()

    print("Front:", q.get_front())
    print("Rear:", q.get_rear())

    q.dequeue()
    q.dequeue()

    q.display()

    print("Is Empty:", q.is_empty())
    print("Is Full:", q.is_full())

main()

