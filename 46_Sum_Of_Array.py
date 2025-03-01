def sum_of_array(arr,i):
    if (len(arr) == i):
        return 0
    
    return sum_of_array(arr,i+1) + arr[i]

s = list(map(int , input("Enter an array \n").split()))
print(sum_of_array(s,0))