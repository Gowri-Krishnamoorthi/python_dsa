# Here’s a complete implementation of a Deque (Double-Ended Queue) using a Doubly Linked List in Python.

# ✅ Features Implemented:
# offer_first(data) – Add at front

# offer_last(data) – Add at rear

# poll_first() – Remove from front

# poll_last() – Remove from rear

# peek_first() – View front

# peek_last() – View rear

# is_empty() – Check if empty

# size() – Return current size

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def offer_first(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self._size += 1

    def offer_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def poll_first(self):
        if self.is_empty():
            print("Deque is empty")
            return None
        removed_data = self.front.data
        self.front = self.front.next
        if self.front:
            self.front.prev = None
        else:
            self.rear = None  # Deque becomes empty
        self._size -= 1
        return removed_data

    def poll_last(self):
        if self.is_empty():
            print("Deque is empty")
            return None
        removed_data = self.rear.data
        self.rear = self.rear.prev
        if self.rear:
            self.rear.next = None
        else:
            self.front = None  # Deque becomes empty
        self._size -= 1
        return removed_data

    def peek_first(self):
        if self.is_empty():
            return None
        return self.front.data

    def peek_last(self):
        if self.is_empty():
            return None
        return self.rear.data

# Example usage
def main():
    dq = Deque()
    dq.offer_last(10)
    dq.offer_first(20)
    dq.offer_last(30)
    dq.offer_first(40)

    print("Front:", dq.peek_first())  # 40
    print("Rear:", dq.peek_last())    # 30
    print("Size:", dq.size())         # 4

    print("Poll First:", dq.poll_first())  # 40
    print("Poll Last:", dq.poll_last())    # 30
    print("Size after polling:", dq.size())  # 2

    print("Is Empty?", dq.is_empty())  # False

main()
