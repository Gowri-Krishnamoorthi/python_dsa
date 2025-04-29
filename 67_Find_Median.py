def find_median(ar1,ar2):
    i,j,k = 0,0,0
    m=[]

    while i<len(ar1) and j<len(ar2):
        if ar1[i] < ar2[j]:
            m.append(ar1[i])
            i = i+1
            k = k+1
        else:
            m.append(ar2[j])
            j = j+1
            k = k+1


    while i<len(ar1):
        m.append(ar1[i])
        i = i+1
        k = k+1

    while j<len(ar2):
        m.append(ar2[j])
        j = j+1
        k = k+1

    mid = len(m) // 2
    if len(m) % 2 == 0:
        return (m[mid] + m[mid-1])/2
    else:
        return m[mid]
    
def main():
    ar1 = [1,3,8,17]
    ar2 = [5,6,7,19,21,25]
    print(find_median(ar1,ar2))

main()

