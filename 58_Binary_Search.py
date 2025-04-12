def binary_search(arr,key):
    low , high , mid = 0 , len(arr)-1 , 0

    while(low<=high):
        #mid = (low+high)//2
        mid = low + (high - low) // 2
        if arr[mid] == key:
           return mid
        elif arr[mid] > key:
            high = mid - 1
            #low = low
        else:
            low = mid + 1
            #high = high
    return -1

def main():
    arr = [14,5,67,89,2,3,0]
    arr.sort()
    print("Sorted array:", arr)
    print(binary_search(arr,89))
main()

