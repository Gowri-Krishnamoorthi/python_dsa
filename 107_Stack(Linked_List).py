class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None  # top points to the head node
        self._size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        popped = self.top.data
        self.top = self.top.next
        self._size -= 1
        return popped

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size

    def display(self):
        curr = self.top
        print("Stack (top -> bottom):", end=" ")
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()


def main():
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.display()

    print("Top:", s.peek())
    print("Pop:", s.pop())
    s.display()

    print("Is Empty:", s.is_empty())
    print("Size:", s.size())

if __name__ == "__main__":
    main()
