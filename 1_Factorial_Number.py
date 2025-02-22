def factorial(x):
    res = 1 # (0!=1)
    for i in range(1,(x+1)):
        res *= i
    return res

def main():
    num = int(input("Enter a Number \n"))
    print(factorial(num))

if __name__ == '__main__':
    main()