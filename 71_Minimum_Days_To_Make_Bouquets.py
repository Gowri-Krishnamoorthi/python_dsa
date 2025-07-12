def is_possible_soln(ar,boq,flowers,m):
    adj , bc = 0 , 0

    for i in ar:
        if i <= m:
           adj = adj + 1
           if adj == flowers:
                bc = bc + 1
                if bc == boq:
                   return True
                adj = 0
        else:
            adj = 0
    return False

def min_day_to_make_bouquets(ar,boq,flowers):
    if boq * flowers > len(ar):
        return -1
    
    l = ar[0]
    h = ar[0]
    # for i in ar:
    #     if i > h:
    #         h = i
    #     if i < l:
    #         l = i
    l = min(ar)
    h = max(ar)
    res = -1

    while l <= h:
        m = l + (h-l)//2

        if is_possible_soln(ar,boq,flowers,m) == True:
            res = m
            h = m - 1
        else:
            l = m + 1

    return res

def main():
    ar = [2,5,2,9,3,10,4,6,5,6]
    boq = 4
    flowers = 2
    print(min_day_to_make_bouquets(ar,boq,flowers))

main()