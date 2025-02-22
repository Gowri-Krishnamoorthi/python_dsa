#Least common multiple

def find_lcm (a,b):
    res = max(a,b)
    while(True):
        if (res%a == 0 and res%b == 0):
            break
        res = res + 1
    return res
        
def main():
    lst= input("Enter a number \n").split()
    print(find_lcm(int(lst[0]),int(lst[1])))

if __name__ == '__main__':
    main()