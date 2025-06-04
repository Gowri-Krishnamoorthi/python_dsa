# A stack is a linear data structure that follows the LIFO (Last In, First Out) principle — 
# the last element added is the first one to be removed.

# 🔑 Key Stack Operations
# Operation	Description
# push(x)	Add element x to the top
# pop()	Remove and return the top element
# peek() / top()	Return the top element without removing it
# is_empty()	Check if the stack is empty
# size()	Return the number of elements

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        print("Stack (top -> bottom):", self.stack[::-1])

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
