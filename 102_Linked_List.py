'''
LinkedList Properties

1.Every Linked List will have a reference called as head and head will always point to the first element or to null 
   if the listed list is empty .
   2.List List is a collection of nodes & every nodes has two parts
   3.The next part of the last node will always NULL
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_linkedlist(self):
        curr = self.head

        while (curr != None):
            print(curr.data , end = ' ')
            curr = curr.next
        print()

    def add(self,e):
        temp = Node(e)
        if (self.head == None):
            self.head = temp
        else:
            curr = self.head
            while(curr.next != None):
                curr = curr.next
            curr.next = temp

    def add_first(self,e):
        temp = Node(e)
        if (self.head == None):
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp

    def add_element_at(self,index,element):
        try:
            if(index == 0):
                self.add_first(element)
            else:
                temp = Node(element)
                count = 0
                curr = self.head

                while (count < (index - 1)):
                    curr = curr.next
                    count = count + 1

                temp.next = curr.next
                curr.next = temp
        except AttributeError:
            raise IndexError('Index ' + str(index) + ' does not exists')
        
    def add_all(self,elements):
        for element in elements:
            self.add(element)

    def remove_first(self):
        if (self.head == None):
            print("No element in Linked List")
        elif self.head.next == None:
              self.head = None
        elif self.head != None:
            curr = self.head
            self.head = self.head.next
            curr.next = None
             
    def remove_last(self):
        if(self.head == None):
            print('No Elements in Linked List')
        elif self.head.next == None:
            self.head = None
        elif self.head.next != None:
            curr = self.head
            while(curr.next.next != None):
                curr = curr.next
            curr.next = None

    def index_of(self,element):
        curr = self.head
        count = 0

        while(curr != None):
            if(curr.data == element):
                return count
            curr = curr.next
            count = count + 1
        
        return -1 
    
    def last_index_of(self,element):
        curr = self.head
        count = 0
        index = -1

        while(curr != None):
            if(curr.data == element):
                index = count
            curr = curr.next
            count = count + 1
        
        return index
    
    def size_of(self):
        curr = self.head
        count = 0

        while(curr != None):
            curr = curr.next
            count += 1
        
        return count

def main():
    ll = LinkedList()

    # p1 = Node(10)
    # p2 = Node(20)
    # p3 = Node(30)
    # p4 = Node(40)

    # ll.head = p1
    # p1.next = p2
    # p2.next = p3
    # p3.next = p4

    ll.add(10)
    ll.add(20)
    ll.add(30)
    ll.add(40)

    ll.add_first(0)

    ll.add_element_at(3,25)
    ll.add_element_at(1,5)

    #ll.add_element_at(20,5) #index error
    elements = [11,22,33,33]
    ll.add_all(elements)
    #ll.add_all([11,22,33,44])
    ll.print_linkedlist()

    #ll.remove_first()
    #ll.remove_last()

    print(ll.index_of(33))

    print(ll.last_index_of(33))

    ll.print_linkedlist()

    print(ll.size_of())

if __name__ == '__main__':
    main()

# #disadvanges 

# add(e) - 0(n)
# removelast - 0(n)
# Reverse Transveral is not possible
