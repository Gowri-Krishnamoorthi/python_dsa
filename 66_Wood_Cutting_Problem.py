def find_wood_count(ht,m):
    wc = 0
    for i in ht:
        if i > m:
            wc = wc + (i-m)
    
    return wc

def find_maxHeight(ht,b):
    max = 0
    for i in ht:
        if max < i:
            max = i
    
    l , h, m = 0 , max  , 0
    
    while(l<=h):
        m = l + (h-l)//2
        wc = find_wood_count(ht,m)

        if wc == b or l== m:
            return m
        elif wc > b:
            l=m
        else:
            h=m

    return -1

def main():
    ht = [20,15,10,17]
    b = 7
    print(find_maxHeight(ht,b))

main()