def count_smaller_equal(arr, key):
    low, high = 0, len(arr) - 1
    result = -1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] <= key:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result + 1

def count_greater_equal(arr, key):
    low, high = 0, len(arr) - 1
    result = -1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] >= key:
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    if result == -1:
        return 0
    return len(arr) - result


def main():
    arr = [1, 2, 2, 2, 3, 5, 6]
    print(count_smaller_equal(arr,6))
    print(count_greater_equal(arr,6))

main()

