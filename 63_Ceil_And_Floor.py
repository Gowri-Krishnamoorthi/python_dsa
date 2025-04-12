def ceil(arr,key):
    low , high , mid = 0 , len(arr)-1 , 0

    while(low<=high):
        #mid = (low+high)//2
        mid = low + (high - low) // 2
        if arr[mid] == key:
           return arr[mid]
        elif arr[mid] > key:
            high = mid - 1
            #low = low
        else:
            low = mid + 1
            #high = high
    if low < len(arr):
        return arr[low]
    else:
        return -1
    
def floor(arr,key):
    low , high , mid = 0 , len(arr)-1 , 0

    while(low<=high):
        #mid = (low+high)//2
        mid = low + (high - low) // 2
        if arr[mid] == key:
           return arr[mid]
        elif arr[mid] > key:
            high = mid - 1
            #low = low
        else:
            low = mid + 1
            #high = high
    if high >= 0:
        return arr[high]
    else:
        return -1
    
def main():
    arr = [19,23,56,61,72,88,92]
    print(ceil(arr,68))
    print(floor(arr,70))

main()