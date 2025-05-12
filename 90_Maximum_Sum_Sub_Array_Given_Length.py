#finding the maximum sum subarray finding the givien length k
#nave apporach

# def max_sum_sub_array(a, k):
#     max_sum = float('-inf')

#     for i in range(0, len(a) - k + 1):
#         current_sum = 0
#         for j in range(i, i + k):
#             current_sum += a[j]
#         max_sum = max(current_sum, max_sum)

#     return max_sum

#sliding window approach 
def max_sum_sub_array(a, k):
    
    if len(a) < k:
        return "Invalid: window size k is larger than array"
    
    window_sum = sum(a[:k])
    max_sum = window_sum

    for i in range(k,len(a)):
        window_sum = window_sum - a[i-k] + a[i]
        max_sum = max(window_sum , max_sum)
    return max_sum

def main():
    a = [2, 9, 31, -4, 21, 7]
    k = 3
    print(max_sum_sub_array(a, k))

main()
