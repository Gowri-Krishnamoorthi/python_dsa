def is_consecutive(n):
    return (n & (n<<1) != 0)

def main():
    num = int(input("Enter a Number \n"))
    print(is_consecutive(num))

main()