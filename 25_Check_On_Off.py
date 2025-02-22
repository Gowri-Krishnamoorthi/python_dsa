def main():
    n = int(input("Enter a Number \n"))
    i = 5
    c_mask = 1 << i

    if ((n&c_mask)==0):
        print("OFF")
    else:
        print("ON")

main()