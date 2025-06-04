class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        removed = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return removed

    def get_front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.front.data

    def get_rear(self):
        if self.is_empty():
            return "Queue is empty"
        return self.rear.data

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue elements:", end=' ')
        current = self.front
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

def main():
    q = LinkedListQueue()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)

    q.display()

    print("Front:", q.get_front())
    print("Rear:", q.get_rear())

    q.dequeue()
    q.dequeue()

    q.display()

    print("Is Empty:", q.is_empty())

main()
