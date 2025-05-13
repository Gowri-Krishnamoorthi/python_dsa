#print matrix in zigzag format
# def matrix(a): #normally it will print
#     for i in range(0,len(a)):
#         for j in range(0,len(a[i])):
#             print(a[i][j],end=" ")
#         print()

def matrix(a): #normally it will print
    for i in range(0,len(a)):
        if i % 2 == 0:
            for j in range(0,len(a[i])):
                print(a[i][j],end=" ")
        else:
            for j in range(len(a[i])-1,-1,-1):
                print(a[i][j],end=" ")
        print()

def main():
    a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    matrix(a)
main()