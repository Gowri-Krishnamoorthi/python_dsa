#Find all the prime factors of a given number(o(n))

def prime_factor(n):
    i = 2
    while (n>1):
        while(n%i==0):
            print(i)
            n = n//i
        i +=1

def main():
    num = int(input("Enter a Number\n"))
    prime_factor(num)

if __name__ == '__main__':
    main()