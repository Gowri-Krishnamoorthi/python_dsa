import math

#o(root n ) only but elliminating the more values 

def is_prime(num):
    if num==1:
       return False
    if num==2 or num==3:
        return True
    if num%2==0 or num%3==0:
        return False
    for i in range (5,int(math.sqrt(num))+1,6):
        if num%i==0 or num%(i+1)==0:
           return False
    return True

def main():
    num = int(input("Enter a Number \n"))
    print(is_prime(num))

if __name__ == '__main__':
    main()