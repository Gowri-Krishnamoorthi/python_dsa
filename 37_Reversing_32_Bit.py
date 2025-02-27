#time o(log N)

def reverse_binary(n):
    f = 31
    l = 0
    rev = 0

    while (f>l):
        if ((n & (1<<f)) != 0):
            rev = rev | (1<<l)
        if ((n & (1<<l)) != 0):
            rev = rev | (1<<f)
        f = f - 1
        l = l + 1

    return rev

def main():
    n = int(input("Enter a Number \n"))
    print(reverse_binary(n))

main()