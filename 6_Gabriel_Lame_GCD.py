# brute force apporach 

def find_gcd (a,b):
    while(a!=0 and b!=0):
        if (a>b):
            a = a%b
        else:
            b = b%a
    return a if a!=0 else b

    # if (a!=0):
    #     return a
    # else:
    #     return b
        
def main():
    lst= input("Enter a number \n").split()
    print(find_gcd(int(lst[0]),int(lst[1])))

if __name__ == '__main__':
    main()