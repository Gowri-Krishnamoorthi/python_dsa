def second_smallest(arr):
    max1 , max2 = 0 , 0

    if arr[0] < arr[1]:
        max1 , max2 = arr[0], arr[1]
    else:
        max1 , max2 = arr[1], arr[0]

    for i in range(2,len(arr)):
        if max1 > arr[i]:
           max2 , max1 = max1 , arr[i]
        elif max2 > arr[i]:
            max2 = arr[i]

    return max2

def main():
    arr = [20,42,6,25,30,88]
    print(second_smallest(arr))

main()