def is_possible_soln(ar,a,m):
    painters = 1
    pbc = 0

    for i in ar:
        if m < i:
            return False
        if pbc + i <= m:
            pbc = pbc + i
        else:
            painters = painters + 1

            if painters > a:
                return False
            pbc = i

    return True

def max_time(ar,a,b):
    l = 0
    h = 0
    
    res = -1

    # for i in ar:
    #     h = h + i

    h = sum(ar)

    while l <= h:
        m = l + (h-l)//2
        
        if is_possible_soln(ar,a,m) == True:
            res = m
            h = m - 1
        else:
            l = m + 1
    
    return res * b

def main():
    ar = [10,20,30,40]
    a = 2
    b = 2
    print(max_time(ar,a,b))

main()
