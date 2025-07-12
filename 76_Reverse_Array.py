def reverse(ar):
    i , j = 0 , len(ar) - 1

    while i < j:
        #   temp = ar[i]
        #   ar[i] = ar[j]
        #   ar[j] = temp
          ar[i] , ar[j] = ar[j] , ar[i]
          i = i + 1
          j = j - 1

def main():
    ar = [2,4,6,8,10,12,14]
    print(ar)
    reverse(ar)
    print(ar)

main()
