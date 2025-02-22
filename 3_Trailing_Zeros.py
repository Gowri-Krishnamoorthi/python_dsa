# Given a number find the number of trailing zeros of its factorial
#input 10

def trailing_zero(num):
    res = 0
    power_of_5 = 5

    while (num >= power_of_5):
        res = res + (num//power_of_5)
        power_of_5 = power_of_5 * 5
    return res

def main():
    num = int(input("Enter a Number \n"))
    print(trailing_zero(num))

if __name__ == '__main__':
    main()