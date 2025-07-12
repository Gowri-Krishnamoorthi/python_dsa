#only square matrix
# import numpy as np
# transposed = np.transpose(matrix)

def transpose_nonsquare(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Sanity check
    for row in matrix:
        if len(row) != cols:
            raise ValueError("All rows must have the same number of columns.")
    
    return [[matrix[i][j] for i in range(rows)] for j in range(cols)]


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    ar = [
        [1, 6, 11, 16, 21, 61],
        [2, 7, 12, 17, 22, 60],
        [3, 8, 13, 18, 23, 62],
        [4, 9, 14, 19, 24, 64],
        [5, 10, 15, 20, 25, 70]
    ]
    print("Original:")
    print_matrix(ar)
    
    res = transpose_nonsquare(ar)
    
    print("\nTransposed:")
    print_matrix(res)

main()
