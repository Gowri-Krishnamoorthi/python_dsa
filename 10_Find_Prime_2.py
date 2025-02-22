#second apporach o(math.square n)

import math


def is_prime(num):
    for i in range (2,int(math.sqrt(num))+1):
        if num%i==0:
           return False
    return True

def main():
    num = int(input("Enter a Number \n"))
    print(is_prime(num))

if __name__ == '__main__':
    main()
