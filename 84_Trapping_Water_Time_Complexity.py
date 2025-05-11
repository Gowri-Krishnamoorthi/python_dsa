#0(n)
def trap(a):
    n = len(a)
    if n <= 2:
        return 0

    if all(a[i] <= a[i + 1] for i in range(n - 1)):
        return 0
    if all(a[i] >= a[i + 1] for i in range(n - 1)):
        return 0

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = a[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], a[i])

    right_max[-1] = a[-1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], a[i])

    res = 0
    for i in range(1, n - 1):
        wl = min(left_max[i - 1], right_max[i + 1])
        if wl > a[i]:
            res += wl - a[i]
    return res
def main():
    a = [4,2,0,3,2,5]
    print(trap(a))
main()