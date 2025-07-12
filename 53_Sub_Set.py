#given a set of non negative integers, and a value sum , determine the number of 
#subsets of the given set with sum equal to given sum

def count_subsets(arr, sum, i):

    if sum == 0:
        return 1
    if sum < 0 :
        return 0
    if i == len(arr):
        return 0
    
    return count_subsets(arr , sum - arr[i] , i+1) + count_subsets(arr, sum , i+1)

def main():
    ar = [10,15,20,5]
    print(count_subsets(ar,25,0))

main()