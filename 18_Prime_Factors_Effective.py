#Find all the prime factors of a given number(o(root n * log(n)))
import math


def prime_factor(n):
    i = 2
    while(i<=math.sqrt(n)):
        while(n%i==0):
            print(i)
            n = n//i
        i +=1
    if n>1:
        print(n)

def main():
    num = int(input("Enter a Number\n"))
    prime_factor(num)

if __name__ == '__main__':
    main()