def power_of(x,y):

    if y == 0:
       return 1
    
    if y % 2 == 0:
       res = power_of(x,y//2)
       return res * res
    else:
       return power_of(x,y-1) * x
    
def main():
   print(power_of(5,2))

main()