#Find the closet smallest element towards the left of the given array

def nearest_smaller_to_left(arr):
    result = []
    stack = []

    for num in arr:
        while stack and stack[-1] >= num:
            stack.pop()
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])
        stack.append(num)

    return result

# Example usage
arr = [4, 5, 2, 10, 8]
print("Input:", arr)
print("Output:", nearest_smaller_to_left(arr))
