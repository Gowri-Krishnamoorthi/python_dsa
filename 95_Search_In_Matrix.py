'''write an efficient algorithm that searches for a target value in an 
m*n integer matrix. THe matrix has following properties
1. integer in each row are stored in ascending from left to right
2. integer in each column are sorted in ascending from top to bottom'''

def search_matrix(a,target):
    i = 0
    j = len(a[0])-1

    while (i < len(a) and j >= 0):
        if a[i][j] == target:
            return True
        elif target < a[i][j]:
            j = j - 1
        else:
            i = i + 1
    return False

def main():
    a = [
        [1,  2,  3,  4],
        [5,  6,  7,  8],
        [9, 10, 11, 12],
        [13,14, 15,16],
        [17,18, 19,20]
    ]
    print(search_matrix(a,0))

main()