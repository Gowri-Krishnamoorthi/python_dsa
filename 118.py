def zoho(n):
    odd = 1
    even = 2
    for i in range(1,n+1):
        for j in range(i):
            if i % 2 == 0:
                print(even, end=' ')
                even += 2
            else:
                print(odd, end=' ')
                odd += 2
        print()
zoho(7)

  

