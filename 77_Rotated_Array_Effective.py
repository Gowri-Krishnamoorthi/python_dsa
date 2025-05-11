def reverse(a,start,end):

    while start < end:
        # temp = a[start]
        # a[start] = a[end]
        # a[end] = temp
        a[start] , a[end] = a[end] , a[start]
        start = start + 1
        end = end -1

def rotate(ar,k):
    if k < 0:
        k = k + len(ar)
    
    k = k % len(ar)

    reverse(ar, 0 , k-1)
    reverse(ar, k , len(ar)-1)    
    reverse(ar, 0 , len(ar)-1)

def main():
    ar = [1,2,3,4,5]
    print(ar)
    rotate(ar,-1)
    print(ar)

main()