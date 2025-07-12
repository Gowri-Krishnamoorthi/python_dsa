#given a bitonic sequence A of N distint elements, write a program to find
#a given element B in the biotonic sequence in 0(log N) time


def ascending_binary_search(arr,key):
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

def decending_binary_search(arr,key):
    low , high , mid = 0 , len(arr)-1 , 0

    while(low<=high):
        #mid = (low+high)//2
        mid = low + (high - low) // 2
        if arr[mid] == key:
           return mid
        elif arr[mid] > key:
            low = mid + 1
            #low = low
        else:
            high = mid - 1
            #high = high
    return -1

def bitonic_element(a):
    l, r = 0, len(a) - 1

    while l <= r:
        m = l + (r - l) // 2

        # Check if m is the bitonic peak
        if (m == 0 or a[m] > a[m - 1]) and (m == len(a) - 1 or a[m] > a[m + 1]):
            return m  # Index of the bitonic peak

        # If the middle is in increasing part
        elif m < len(a) - 1 and a[m] < a[m + 1]:
            l = m + 1
        else:
            r = m - 1

    return -1  # Should never happen if input is bitonic

def main():
    a = [5,6,7,8,9,10,3,2,1]
    key = 1
    bitonic_index = bitonic_element(a)

    if a[bitonic_index] == key:
        print(bitonic_index)
    else:
        index = ascending_binary_search(a[:bitonic_index+1], key)
        if index != -1:
            print(index)
        else:
            index = decending_binary_search(a[bitonic_index+1:], key)
            if index != -1:
                print(bitonic_index + 1 + index)
            else:
                print(-1)

main()
