# brute force apporach 

def find_gcd (a,b):
    min = 0
    if (a > b):
        min = b
    else:
        min = a

    for i in range(min ,0 ,-1):
        if (a % i == 0) and (b % i == 0):
            return i
        
def main():
    lst= input("Enter a number \n").split()
    print(find_gcd(int(lst[0]),int(lst[1])))

if __name__ == '__main__':
    main()