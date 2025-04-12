def liner_search(a,key):
    for i in range(0,len(a)):
        if key == a[i] :
           return i
        
    return -1

def main():
    a = [10,20,50,77,90]
    key = 99
    print(liner_search(a,key))

main()