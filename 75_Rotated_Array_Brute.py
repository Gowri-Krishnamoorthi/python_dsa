def rotate_one(ar):
    temp = ar[0]

    for i in range(1,len(ar)):
        ar[i-1] = ar[i]
     
    ar[len(ar) - 1] = temp

def rotate(ar,k):
    if k < 0:
        k = k + len(ar)

    k = k % len(ar)

    for i in range(k):
        rotate_one(ar)

def main():
    ar = [1,2,3,4,5]
    print(ar)
    rotate(ar,-1)
    print(ar)

main()