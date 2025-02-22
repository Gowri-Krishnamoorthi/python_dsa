def check_power_of_2(num):
    if num == 0:
        return False
    
    return num&(num-1) == 0

def main():
    num = int(input("Enter a Number \n"))
    print(check_power_of_2(num))

main()