def spiralOrder(matrix):
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    result = []
    while top <= bottom and left <= right:
        # Traverse from Left to Right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Traverse from Top to Bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Check if bounds are still valid
        if not (top <= bottom and left <= right):
            break

        # Traverse from Right to Left
        for i in range(right, left - 1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1

        # Traverse from Bottom to Top
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1

    return result

def main():
    matrix = [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [9, 10, 11, 12, 13, 14, 15, 16],
        [17, 18, 19, 20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29, 30, 31, 32],  # Fixed this row (removed duplicate 31)
        [33, 34, 35, 36, 37, 38, 38, 40],
        [41, 42, 43, 44, 45, 46, 47, 48]
    ]
    print(spiralOrder(matrix))

main()
