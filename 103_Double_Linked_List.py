class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


def main():
    temp = Node(10)
    print(temp.data)    
    print(temp.prev)    
    print(temp.next)

if __name__ == '__main__':
    main()