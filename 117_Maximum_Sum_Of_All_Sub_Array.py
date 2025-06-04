#Find the maximum number of all sub arrays of size k
from collections import deque

def max_subarrays(arr, k):
    if k > len(arr):
        return []

    dq = deque()  # stores indices
    result = []

    for i in range(len(arr)):
        # Remove elements not in current window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove elements smaller than current from the rear
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        dq.append(i)

        # Start adding to result after first k elements
        if i >= k - 1:
            result.append(arr[dq[0]])

    return result

# Example usage
arr = [10, 5, 2, 7, 8, 7]
k = 3
print(max_subarrays(arr, k))
