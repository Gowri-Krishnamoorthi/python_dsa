class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("List is empty")
            return
        curr = self.head
        while True:
            print(curr.data, end=' ')
            curr = curr.next
            if curr == self.head:
                break
        print()

    def print_backward(self):
        if self.head is None:
            print("List is empty")
            return
        curr = self.head.prev  # last node
        while True:
            print(curr.data, end=' ')
            curr = curr.prev
            if curr == self.head.prev:
                break
        print()

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node.prev = new_node
            self.head = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def add_first(self, data):
        self.add(data)
        self.head = self.head.prev

    def remove_first(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            tail = self.head.prev
            self.head = self.head.next
            self.head.prev = tail
            tail.next = self.head

    def remove_last(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            tail = self.head.prev
            new_tail = tail.prev
            new_tail.next = self.head
            self.head.prev = new_tail

    def size(self):
        if self.head is None:
            return 0
        count = 0
        curr = self.head
        while True:
            count += 1
            curr = curr.next
            if curr == self.head:
                break
        return count

def main():
    cdll = CircularDoublyLinkedList()

    cdll.add(10)
    cdll.add(20)
    cdll.add_first(5)
    cdll.add(30)

    print("Forward:")
    cdll.print_forward()

    print("Backward:")
    cdll.print_backward()

    print("Size:", cdll.size())

    cdll.remove_first()
    cdll.remove_last()

    print("After Deletions:")
    cdll.print_forward()

if __name__ == "__main__":
    main()
