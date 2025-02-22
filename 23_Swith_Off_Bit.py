def main():
    n = int(input("Enter a Number \n"))
    i = 5
    off_mask = ~(1<<i)
    print(n & off_mask)

main()