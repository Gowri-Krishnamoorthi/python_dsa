def count_digits(n):
    if n == 0:
        return n
    
    return count_digits(n//10) + n%10

n = int(input("Enter a Number \n"))
print(count_digits(n))