#time o (log N)

def max_consecutive(n):
    count = 0

    while(n>0):
        n = n & (n<<1)
        count += 1

    return count

def main():
    num = int(input("Enter a Number \n"))
    print(max_consecutive(num))

main()