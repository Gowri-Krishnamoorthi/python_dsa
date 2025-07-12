def count_digits(n):
    if n == 0:
        return n
    
    return count_digits(n//10) + n%10

# def count_digits(n):
#     res = 0
#     while n > 0:
#         res = res + n % 10
#         n = n // 10
#     return res
n = int(input("Enter a Number \n"))
print(count_digits(n))