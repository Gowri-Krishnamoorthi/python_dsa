def permutations(ar , fi):

    if (fi == len(ar)-1):
        print("".join(ar))
        return
    
    for i in range(fi , len(ar)):
        ar[fi] , ar[i]= ar[i] , ar[fi]
        permutations(ar , fi+1)
        ar[fi] , ar[i]= ar[i] , ar[fi]

def main():
    s = input()
    permutations (list(s) , 0)

main()