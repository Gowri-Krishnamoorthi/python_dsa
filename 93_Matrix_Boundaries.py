#n*n matrix
def matrix_boundaries(a):
    n = len(a)  # since it's a square matrix

    # Top row
    for j in range(n):
        print(a[0][j], end=" ")

    # Right column (excluding top element)
    for i in range(1, n):
        print(a[i][n - 1], end=" ")

    # Bottom row (excluding last element of right column)
    for j in range(n - 2, -1, -1):
        print(a[n - 1][j], end=" ")

    # Left column (excluding first and last elements)
    for i in range(n - 2, 0, -1):
        print(a[i][0], end=" ")

    print()  # For newline

def print_boundary_box(a):
    n = len(a)  # For n x n matrix

    for i in range(n):
        for j in range(n):
            # Top row
            if i == 0:
                print(a[i][j], end=" ")

            # Bottom row
            elif i == n - 1:
                print(a[i][j], end=" ")

            # Left and right columns
            elif j == 0 or j == n - 1:
                print(a[i][j], end=" ")

            # Inner elements
            else:
                print("  ", end=" ")  # spacing to keep format
        print()  # Move to next line

def main():
    a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    matrix_boundaries(a)
    print_boundary_box(a)
main()