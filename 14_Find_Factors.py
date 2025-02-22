#0(n)

def find_factors(num):
    for i in range(1,num+1):
        if(num%i==0):
            print(i)

def main():
    num = int(input("Enter a Number \n"))
    find_factors(num)

main()