def matrix_boundaries(a):
    rows = len(a)
    cols = len(a[0])

    # Top row
    for j in range(cols):
        print(a[0][j], end=" ")

    # Right column (excluding top)
    for i in range(1, rows):
        print(a[i][cols - 1], end=" ")

    # Bottom row (excluding rightmost, only if more than 1 row)
    if rows > 1:
        for j in range(cols - 2, -1, -1):
            print(a[rows - 1][j], end=" ")

    # Left column (excluding top and bottom, only if more than 1 col)
    if cols > 1:
        for i in range(rows - 2, 0, -1):
            print(a[i][0], end=" ")

    print()  # Newline

def print_boundary_box(a):
    rows = len(a)
    cols = len(a[0])

    for i in range(rows):
        for j in range(cols):
            # Top row
            if i == 0:
                print(f"{a[i][j]:<3}", end=" ")

            # Bottom row
            elif i == rows - 1:
                print(f"{a[i][j]:<3}", end=" ")

            # Left and right columns
            elif j == 0 or j == cols - 1:
                print(f"{a[i][j]:<3}", end=" ")

            # Inner elements (blank)
            else:
                print("    ", end=" ")
        print()

def main():
    a = [
        [1,  2,  3,  4],
        [5,  6,  7,  8],
        [9, 10, 11, 12],
        [13,14, 15,16],
        [17,18, 19,20]
    ]
    
    print("Flat boundary traversal:")
    matrix_boundaries(a)

    print("\nVisual boundary box:")
    print_boundary_box(a)

main()
