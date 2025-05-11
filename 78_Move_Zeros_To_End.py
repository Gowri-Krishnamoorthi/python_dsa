def move_zeros(ar):
    if len(ar) == 0 or len(ar) == 1:
        return
    
    z , nz = 0 , 0

    while nz < len(ar):
        if ar[nz] != 0:
            ar[z] , ar[nz] = ar[nz] , ar[z]
            nz = nz + 1
            z = z + 1
        else:
            nz = nz + 1

def main():
    #nums = [0,1,0,3,12]
    nums = [5,10,22,8,0,5,0]
    move_zeros(nums)
    print(nums)
main()