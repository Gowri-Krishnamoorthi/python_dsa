def fibonacci_series(n):
    if n == 1 or n == 2:
        return 1
    
    return fibonacci_series(n-1) + fibonacci_series(n-2)

def main():
    n = int(input("Enter a Number \n"))
    print(fibonacci_series(n))

main()

