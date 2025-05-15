def reverse_matrix(ar):
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
    ar = [
        [1, 6, 11, 16, 21],
        [2, 7, 12, 17, 22],
        [3, 8, 13, 18, 23],
        [4, 9, 14, 19, 24],
        [5, 10, 15, 20, 25]
    ]
    print("Original:")
    print_matrix(ar)

    reverse_matrix(ar)
    print("\nAfter reversing rows:")
    print_matrix(ar)

main()
