def factorial(x):
    # res = 1 # (0!=1)
    # for i in range(1,(x+1)):
    #     res *= i
    # return res
    if x == 0:
        return 0
    if x == 1:
        return 1
    return x * factorial(x-1)

def main():
    num = int(input("Enter a Number \n"))
    print(factorial(num))

if __name__ == '__main__':
    main()