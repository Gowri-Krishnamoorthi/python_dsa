def main():
    #n = 36
    n = int(input("Enter a Number \n"))
    i = 3
    on_mask = 1 << i
    print(n|on_mask)

main()