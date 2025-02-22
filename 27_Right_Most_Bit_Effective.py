import math

def right_most_bit(n):
    # a = n^(n&(n-1))
    # return  a // 8 (we want 2^3 power + 1 should return)
    return  math.log(n^(n&(n-1)),2) + 1

def main():
    n = int(input("Enter a Number \n"))
    print(right_most_bit(n))

main()

