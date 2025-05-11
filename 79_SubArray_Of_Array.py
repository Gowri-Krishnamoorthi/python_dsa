def sub_array(ar):
    for i in range(len(ar)):
        for j in range(i,len(ar)):
            print(ar[i:j+1])

def main():
    a = [1,2,3,4,5]
    sub_array(a)
main()