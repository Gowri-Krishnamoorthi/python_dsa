# o(1)

def swap_ood_even_places(n):
    return ( (n & 0Xaaaaaaaa ) >> 1| ( n & 0X55555555 ) << 1)

def main():
    n = int(input("Enter a Number \n"))
    print(swap_ood_even_places(n))

main()