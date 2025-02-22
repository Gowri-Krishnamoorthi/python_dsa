def count_set_bit(n):
    count = 0
    while (n >0 ):
        n = n & (n-1)
        count +=1
    return count

def main():
    num = int(input("Enter a Number \n"))
    print(count_set_bit(num))

main()