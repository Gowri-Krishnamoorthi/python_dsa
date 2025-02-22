def main():
    n = int(input("Enter a Number \n"))
    i = 5
    t_mask = 1 << i
    print(n ^ t_mask)

main()