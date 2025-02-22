#0(root n)
import math

def find_factors(num):
    for i in range(1,int(math.sqrt(num))+1):
        if (num%i==0):
            print(i)
            '''if i!=(num//i):
                print(num//i)'''
    for i in range(int(math.sqrt(num)),0,-1):
        if (num%i==0 and i!=(num//i)):
            print(num//i)
        
def main():
    num = int(input("Enter a Number \n"))
    find_factors(num)

main()