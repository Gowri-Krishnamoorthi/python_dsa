# nave apporach
# def longest_even_odd_subarray(a):
#     max_count = 1

#     for i in range(len(a)):
#         count = 1
#         for j in range(i+1,len(a)):
#             if (a[j] % 2 == 0 and a[j-1] % 2 !=0) or (a[j] % 2 != 0 and a[j-1] % 2 ==0) :
#                 count = count + 1
#             else:
#                 break

#         max_count = max(count , max_count)
#     return max_count

#effective apporach
def longest_even_odd_subarray(a):
    count = 1
    max_count = 1
    for i in range(1,len(a)):
        if (a[i] % 2 == 0 and a[i-1] % 2 !=0) or (a[i] % 2 != 0 and a[i-1] % 2 ==0) :
            count = count + 1
            max_count = max(count , max_count)
        else:
            count = 1
    
    return max_count

def main():
    a = [8,10,13,14,9,5]
    print(longest_even_odd_subarray(a))
main()
