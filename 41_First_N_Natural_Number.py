def n_natural_number(n):
    if n == 0:
        return
    print(n)
    n_natural_number(n-1)
    #print(n)

n = int(input("Enter a Number \n"))
n_natural_number(n)