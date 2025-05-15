def transpose(ar):
    res = []
    for i in range(0,len(ar)):
        res.append([0]*len(ar))

    for i in range(0,len(ar)):
        for j in range(0,len(ar)):
            res[j][i] = ar[i][j]
    return res

def print_matrix(ar):
     for i in range(0,len(ar)):
        for j in range(0,len(ar)):
            print(ar[i][j] , end = " ")
        print()

def main():
    ar = [[1,6,11,16,21],[2,7,12,17,22],[3,8,13,18,23],[4,9,14,19,24],[5,10,15,20,25]]
    print_matrix(ar)
    res = transpose(ar)
    print()
    print_matrix(res)

main()