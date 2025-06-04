class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = data
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        removed = self.queue[self.front]
        self.queue[self.front] = None  # Optional: Clear the slot
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
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
            return
        print("Queue elements:", end=' ')
        count = 0
        i = self.front
        while count < self.size:
            print(self.queue[i], end=' ')
            i = (i + 1) % self.capacity
            count += 1
        print()

def main():
    q = Queue(5)

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
