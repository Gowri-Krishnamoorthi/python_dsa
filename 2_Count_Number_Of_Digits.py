#write a program to count the number of digits
#input 2597

''' steps 
1. check if the digit exists n>0
2. remove the last digit  n/=10
3. increase the value of count by 1 count+=1
4. Repeat step 1 to step 3 till digits remains
'''

def num_of_digits(num):
    count = 0
    while(num > 0):
        count += 1
        num = num // 10 #floor division for hole number
        print(num)
    return count

def main():
    num = int(input("Enter a Number \n"))
    print(num_of_digits(num))

if __name__ == '__main__':
    main()


# def num_of_digits(num):
#     count = 0
#     for i in num:
#         if i.isdigit:
#             count += 1
#     return count

# def main():
#     num = input("Enter a Number \n")
#     print(num_of_digits(num))

# if __name__ == '__main__':
#     main()
    
