class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print(self):
        curr = self.head
        while(curr != None):
            print(curr.data , end = ' ')
            curr = curr.next
        print()

    def print_reverse(self):
        curr = self.tail
        while(curr != None):
            print(curr.data , end = ' ')
            curr = curr.prev
        print()
    
    def add(self,e):
        temp = Node(e)
        if(self.head == None):
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            temp.prev = self.tail
            self.tail = temp

    def add_first(self,e):
        temp = Node(e)
        if(self.head == None):
            self.head = temp
            self.tail = temp
        else:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp

    def add_at(self, index, element):
        if index < 0:
            raise IndexError("Index cannot be negative")

        temp = Node(element)

        if index == 0:
            self.add_first(element)
            return

        curr = self.head
        count = 0

        while curr is not None and count < index - 1:
            curr = curr.next
            count += 1

        if curr is None:
            raise IndexError("Index out of bounds")

        if curr.next is None:
            # Inserting at the end
            curr.next = temp
            temp.prev = curr
            self.tail = temp
        else:
            # Inserting in the middle
            temp.next = curr.next
            curr.next.prev = temp
            curr.next = temp
            temp.prev = curr

    def add_all(self,elements):
        for element in elements:
            self.add(element)

    def remove_first(self):
        if self.head is None:
            print("List is empty. Nothing to remove.")
            return

        if self.head == self.tail:
            # Only one element in the list
            self.head = None
            self.tail = None
        else:
            # More than one element
            self.head = self.head.next
            self.head.prev = None

    def remove_last(self):
        if self.tail is None:
            print("List is empty. Nothing to remove.")
            return

        if self.head == self.tail:
            # Only one element in the list
            self.head = None
            self.tail = None
        else:
            # More than one element
            self.tail = self.tail.prev
            self.tail.next = None

    def index_of(self, element):
        curr = self.head
        index = 0

        while curr:
            if curr.data == element:
                return index
            curr = curr.next
            index += 1

        return -1  # Element not found
    
    def last_index_of(self, element):
        curr = self.tail
        index = self.size() - 1

        while curr:
            if curr.data == element:
                return index
            curr = curr.prev
            index -= 1

        return -1  # Element not found
    
    def size(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

def main():
    # temp = Node(10)
    # print(temp.data)    
    # print(temp.prev)    
    # print(temp.next)

    dll = DoublyLinkedList()

    dll.add(10)
    dll.add(20)
    dll.add(30)
    dll.add(40)
    dll.add(20)

    dll.add_first(75)

    dll.add_at(2,9)

    dll.add_all([1,2,3,4])

    dll.print()

    print(dll.index_of(20))      # Output: 1
    print(dll.last_index_of(20)) # Output: 3
    print(dll.size())            # Output: 4

    dll.remove_first()
    dll.remove_last()
    # print(dll.head.data)
    # print(dll.tail.data)


    dll.print()
    #dll.print_reverse()

if __name__ == '__main__':
    main()