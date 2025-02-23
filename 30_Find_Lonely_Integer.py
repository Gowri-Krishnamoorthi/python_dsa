# o(N log N) // brute force apporach

def lonely_integer(arr):
    arr.sort()
    for i in range(0,len(arr)-2,2):
        if (arr[i] != arr[i+1]):
            return arr[i]
    return arr[len(arr)-1]

def main():
    arr = list(map(int, input("Enter an array: ").split()))
    print(lonely_integer(arr))

if __name__ == '__main__':
    main()

