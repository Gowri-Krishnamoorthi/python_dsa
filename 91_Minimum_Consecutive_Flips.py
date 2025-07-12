'''we need to convert all zeros or one's using minimum flips'''
'''observation
1. which is one starting that will not contain the minimum flips
2. if both are equal flips any thing we can take , so will take a[i]!=
3. if first a[i] and a[len(a)-1] is not equal it will contain the same number of flips'''
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
    ar = [1,1,0,0,1,1,0,0,0,1,1]
    min_flips(ar)

main()