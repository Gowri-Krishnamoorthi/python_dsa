def sub_array(ar):
    for i in range(len(ar)):
        for j in range(i,len(ar)):
            print(ar[i:j+1])
            
# def sub_array(ar):
#     n = len(ar)
#     for i in range(n):
#         temp = []
#         for j in range(i, n):
#             temp.append(ar[j])
#             print(temp)  # or yield tuple(temp) if you want to return them

def main():
    a = [1,2,3,4,5]
    sub_array(a)
main()