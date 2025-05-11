#nave apporach
# def majorityelement(nums):
#     for i in range(len(nums)):
#         count = 1
#         for j in range(i+1 , len(nums)):
#             if nums[i] == nums[j]:
#                 count = count + 1
#         if (count > len(nums)//2):
#             return nums[i]

def majorityelement(a):
    maj = a[0]
    count = 1

    for i in range(1,len(a)):
        if a[i] == maj:
            count = count + 1
        else:
            count = count - 1
        
        if count == 0:
            maj = a[i]
            count = 1
    return maj
        

def main():
    a = [3,2,3]
    print(majorityelement(a))

main()