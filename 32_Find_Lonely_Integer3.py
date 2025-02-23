# o(N) // but space reduced

def lonely_integer(arr):
    result = 0

    for i in arr:
        result = result ^ i
    
    return result

def main():
    arr = list(map(int, input("Enter an array: ").split()))
    print(lonely_integer(arr))

if __name__ == '__main__':
    main()

