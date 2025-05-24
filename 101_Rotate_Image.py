# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:


# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

def rotate(ar):
    #transpose matrix
    for i in range(0,len(ar)-1):
        for j in range(i+1,len(ar)):
            ar[i][j],ar[j][i] = ar[j][i],ar[i][j]

    #Reverse matrix
    for i in range(len(ar)):
        left = 0
        right = len(ar[i]) - 1
        while left < right:
            ar[i][left], ar[i][right] = ar[i][right], ar[i][left]
            left += 1
            right -= 1

def print_matrix(ar):
    for row in ar:
        print(" ".join(map(str, row)))

def main():
    ar = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    ar = [[1,2,3],[4,5,6],[7,8,9]]
    print_matrix(ar)
    rotate(ar)
    print()
    print_matrix(ar)
main()