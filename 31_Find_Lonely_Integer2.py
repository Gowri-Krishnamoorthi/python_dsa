# o(N) // but space is increased

def lonely_integer(arr):
    s = set()
    for i in arr:
        if i not in s:
            s.add(i)
        else:
            s.remove(i)
    return s.pop()

def main():
    arr = list(map(int, input("Enter an array: ").split()))
    print(lonely_integer(arr))

if __name__ == '__main__':
    main()

