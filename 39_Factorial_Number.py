def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n-1)

def main():
    n = int(input("Enter a Number \n"))
    print(fact(n))

main()

