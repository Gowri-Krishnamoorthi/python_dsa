class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def print_linkedlist(self):
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

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head

    def add_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            new_node.next = self.head
            self.head = new_node
            curr.next = self.head

    def add_element_at(self, index, data):
        if index == 0:
            self.add_first(data)
        else:
            new_node = Node(data)
            curr = self.head
            count = 0
            while count < index - 1:
                curr = curr.next
                if curr == self.head:
                    raise IndexError("Index out of bounds")
                count += 1
            new_node.next = curr.next
            curr.next = new_node

    def add_all(self, elements):
        for element in elements:
            self.add(element)

    def remove_first(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            last = self.head
            while last.next != self.head:
                last = last.next
            self.head = self.head.next
            last.next = self.head

    def remove_last(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            curr = self.head
            prev = None
            while curr.next != self.head:
                prev = curr
                curr = curr.next
            prev.next = self.head

    def index_of(self, value):
        curr = self.head
        index = 0
        if self.head is None:
            return -1
        while True:
            if curr.data == value:
                return index
            curr = curr.next
            index += 1
            if curr == self.head:
                break
        return -1

    def last_index_of(self, value):
        curr = self.head
        index = 0
        last_index = -1
        if self.head is None:
            return -1
        while True:
            if curr.data == value:
                last_index = index
            curr = curr.next
            index += 1
            if curr == self.head:
                break
        return last_index

    def size_of(self):
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
    cll = CircularLinkedList()
    
    cll.add(10)
    cll.add(20)
    cll.add(30)
    cll.add_first(5)
    cll.add_element_at(2, 15)
    cll.add_all([40, 50, 50])

    cll.print_linkedlist()

    print("Index of 50:", cll.index_of(50))
    print("Last index of 50:", cll.last_index_of(50))
    print("Size:", cll.size_of())

    cll.remove_first()
    cll.remove_last()
    cll.print_linkedlist()

if __name__ == '__main__':
    main()
