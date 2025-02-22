# brute force apporach 

def find_gcd (a,b):
    while(a!=b):
        if (a>b):
            a = a-b
        else:
            b = b-a
    return a
        
def main():
    lst= input("Enter a number \n").split()
    print(find_gcd(int(lst[0]),int(lst[1])))

if __name__ == '__main__':
    main()