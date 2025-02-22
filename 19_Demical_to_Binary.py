def decimal_to_binary(n):
    b = ' '
    while(n>=1):
        x = n%2
        n = n//2
        b = str(x) + b
    return b

def main():
    num = int(input("Enter a Number \n"))
    print(decimal_to_binary(num))

if __name__ == '__main__':
    main()