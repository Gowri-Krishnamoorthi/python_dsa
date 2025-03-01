def balanced_parenthesis(arr,n,i,o,c):
    if i == len(arr):
       print("".join(arr))

    if (o<n):
        arr[i] = '('
        balanced_parenthesis(arr,n,i+1,o+1,c)

    if (c<o):
        arr[i] = ')'
        balanced_parenthesis(arr,n,i+1,o,c+1)

    
n = int(input("Enter A Number \n"))

list = [""] * (n*2)

balanced_parenthesis(list,n,0,0,0)
