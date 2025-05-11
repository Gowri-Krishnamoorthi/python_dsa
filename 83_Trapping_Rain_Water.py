# def trap(a):
#     res = 0

#     for i in range(1,len(a)-1):
#         lb = a[i]
#         for j in range(i):
#             if lb < a[j]:
#                 lb = a[j]
#         rb = a[i]
#         for j in range(i+1 , len(a)):
#             if rb < a[j]:
#                 rb = a[j]

#         wl = min(lb,rb)
#         tw = wl - a[i]
#         res = res + tw
#     return res
# this o(n*n)
def trap(a):
    n = len(a)
    if n <= 2:
        return 0  # Not enough bars to trap water

    # Check if array is strictly increasing
    if all(a[i] <= a[i + 1] for i in range(n - 1)):
        return 0

    # Check if array is strictly decreasing
    if all(a[i] >= a[i + 1] for i in range(n - 1)):
        return 0

    res = 0
    for i in range(1, n - 1):
        lb = max(a[:i])          # Left boundary
        rb = max(a[i + 1:])      # Right boundary
        wl = min(lb, rb)         # Water level
        if wl > a[i]:
            res += wl - a[i]
    return res

def main():
    a = [4,2,0,3,2,5]
    print(trap(a))
main()