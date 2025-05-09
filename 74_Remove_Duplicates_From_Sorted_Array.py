def remove_duplicates(ar):
    rd = 0

    for i in range(1,len(ar)):
        if ar[rd] != ar[i]:
            rd = rd + 1
            ar[rd] = ar[i]
    return rd + 1

def main():
    ar = [2,2,3,3,4,5,5,6]
    print(ar)
    rd = remove_duplicates(ar) 
    print(ar[:rd])

main()