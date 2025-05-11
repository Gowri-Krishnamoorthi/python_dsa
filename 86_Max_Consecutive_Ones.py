# navie apporach
# def max_count(a):
#     max_count = 0
#     for i in range(len(a)):
#         count = 0
#         for j in range(i,len(a)):
#             if a[j] == 1:
#                 count = count + 1
#             else:
#                 break
#         max_count = max(max_count,count)
#     return max_count

# effective apporach
def max_count(a):
    max_count = 0
    current_count = 0

    for i in a:
        if i == 1:
            current_count += 1
            max_count = max(current_count , max_count)
        else:
            current_count = 0
    return max_count

def main():
    a = [0,1,1,1,0,0,1,0]
    print(max_count(a))
main()