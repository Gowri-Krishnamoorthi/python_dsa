def sqrt(n):
    if n==0 or n==1:
        return n
    l = 2
    h = n//2

    res = 0

    while l <= h:
        m = l + (h-l)//2

        if m * m == n:
            return m
        elif m * m < n:
            res = m
            l = m + 1
        else:
            h = m - 1
            #res = m // ceil
    return res

def main():
    n = 24
    print(sqrt(n))

main()