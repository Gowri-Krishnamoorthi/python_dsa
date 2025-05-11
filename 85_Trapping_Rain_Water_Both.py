#trapping rain water both time complexity 0(n) and space complexity 0(1)
def trap(height):
    n = len(height)
    if n <= 2:
        return 0

    # Early exit: strictly increasing or decreasing
    if all(height[i] <= height[i + 1] for i in range(n - 1)):
        return 0
    if all(height[i] >= height[i + 1] for i in range(n - 1)):
        return 0

    left = 0
    right = n - 1
    left_max = 0
    right_max = 0
    res = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                res += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                res += right_max - height[right]
            right -= 1

    return res

def main():
    a = [4, 2, 0, 3, 2, 5]
    print(trap(a))  # Output: 9

main()
