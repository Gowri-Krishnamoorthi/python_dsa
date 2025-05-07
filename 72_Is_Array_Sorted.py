def is_sorted(ar):

    for i in range(1, len(ar)):
        if ar[i] < ar[i-1]:
           return False
        
    return True

def main():
    ar = [2,4,6,8,10,12,14]
    print(is_sorted(ar))

main()