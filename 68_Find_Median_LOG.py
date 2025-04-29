import sys


def find_median(ar1,ar2):
    if len(ar1) > len(ar2):
        return find_median(ar2,ar1)
    
    l = 0
    h = len(ar1)

    while l<=h:
        m1 = l + (h-l)//2
        m2 = (len(ar1) + len(ar2) + 1)//2 - m1

        l1 = (sys.maxsize * -1) if (m1==0) else (ar1[m1-1])
        r1 = (sys.maxsize) if (m1==len(ar1)) else (ar1[m1])

        l2 = (sys.maxsize * -1) if (m2==0) else (ar2[m2-1])
        r2 = (sys.maxsize) if (m2==len(ar1)) else (ar2[m2])

        if l1 <= r2 and l2 <= r1:
            if (len(ar1) + len(ar2) ) % 2 == 0:
                return ((max(l1,l2)) + min(r1,r2))/2
            else:
                return (max(l1,l2))
            
        elif l2 > r1:
            l = m1 + 1
        else:
            h = m1 - 1

def main():
    ar1 = [1,3,8,17]
    ar2 = [5,6,7,19,21,25]
    print(find_median(ar1,ar2))

main()