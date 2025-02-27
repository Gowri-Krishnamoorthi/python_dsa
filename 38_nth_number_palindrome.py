# write a program to find the nth number , whose binary representation is a palindrome 

import math

def reverse_binary(n,length):
    f = length - 1
    l = 0
    rev = 0

    while (f>l):
        if ((n & (1<<f)) != 0):
            rev = rev | (1<<l)
        if ((n & (1<<l)) != 0):
            rev = rev | (1<<f)
        f = f - 1
        l = l + 1

    return rev

def nth_palin_binary(n):
    length = 0
    count = 0

    while (count<n):
        length += 1
        count += int(math.pow(2, (length-1)//2))

    count -= int(math.pow(2, (length-1)//2))
    elem = n - count - 1
    ans = ( (1<< (length-1)) | (elem<<(length//2)))
    ans = ans | reverse_binary(ans,length)
    return ans

n = int(input("Enter a Number \n"))
print(bin(nth_palin_binary(n)))
