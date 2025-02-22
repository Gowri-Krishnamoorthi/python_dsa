# Find all the numbers from 1 to n

import math


def find_prime_all(n):
    prime = [False] * (n+1)
    for i in range (2,int(math.sqrt(n))+1):
        if prime[i] == False:
            for j in range(i*i,n+1,i):
                prime[j] = True
    for i in range(2,n+1):
        if(prime[i]==False):
            print(i)
        

def main():
    num = int(input("Enter a Number \n"))
    find_prime_all(num)

if __name__ == '__main__':
    main()