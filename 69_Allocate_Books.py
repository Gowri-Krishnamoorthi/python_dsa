def max_page(ar,b):
    if b > len(ar):
        return -1
    
    l = ar[0]
    h = 0

    # for i in ar:
    #     if l > i:
    #         l = i
    #     h = h + i

    l = max(ar)
    h = sum(ar)

    res = -1
    while l <= h:
        m = (l+h)//2

        if is_possible_sol(ar,b,m) == True:
            res = m
            h = m-1
        else:
            l = m+1

    return res

def is_possible_sol(ar,b,m):
    students = 1
    spc = 0

    for i in ar:
        if i > m:
            return False
        if spc + i <= m:
            spc = spc + i
        else:
            students = students + 1
            if students > b:
                return False
            spc = i

    return True

def main():
    ar = [2,3,4,1]
    b = 2
    print(max_page(ar,b))

main()