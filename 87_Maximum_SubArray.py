'''given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum. a subarray is a contiguous part of an array'''

#KADANE"S ALGORITHM

#nave apporach
# def max_sub_array(ar):
#     max_sum = 0
#     for i in range(len(ar)):
#         sum = 0
#         for j in range(i,len(ar)):
#             sum = sum + ar[j]
#             max_sum = max(sum,max_sum)
#     return max_sum

#effective apporach
def max_sub_array(a):
    max_sum = a[0]
    sum = a[0]

    for i in range(1,len(a)):
        if (sum >= 0):
            sum = sum + a[i]
        else:
            sum = a[i]

        max_sum = max(sum,max_sum)
    return max_sum

def main():
    ar = [5,6,-3,7,-13,8,-2,5,-6,7,-11,3,10,-10,-6,-10,7,2]
    print(max_sub_array(ar))
main()