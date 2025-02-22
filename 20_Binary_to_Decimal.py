def decimal_to_binary(n):
    b = ''
    while(n>=1):
        x = n%2
        n = n//2
        b = str(x) + b
    return b

def binary_to_decimal(b):
    result = 0
    pow_of_2 = 1

    for i in range(len(b)-1, -1 , -1):
        if (b[i]=='1'):
            result = result + pow_of_2
        pow_of_2 = pow_of_2 * 2
    
    return result

def main():
    num = int(input("Enter a Number \n"))
    b = decimal_to_binary(num)
    print(b)
    print(binary_to_decimal(b))

if __name__ == '__main__':
    main()