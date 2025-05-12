def min_flips(ar):
    for i in range(1,len(ar)):
        if ar[i] != ar[i-1]:
            if ar[i] != ar[0]:
                print(i , " ", end=" ")
            else:
                print(i-1)

    if (ar[0] != ar[len(ar)-1]): # filps will be same , so it will not print the last index 
        print(len(ar)-1)

def main():
    ar = [1,1,0,1,1,0,1,0,0,0]
    min_flips(ar)

main()