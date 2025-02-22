def right_most_bit(n):
    m = 1
    pos = 0
    
    while((n&m)==0):
        m = m+1
        pos = pos+1
    return pos+1

def main():
    n = int(input("Enter a Number \n"))
    print(right_most_bit(n))

main()

