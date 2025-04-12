def tower_of_honai(n , src , aux , dest):
    if n == 1:
       print(src,'-->',dest)
       return
    tower_of_honai(n-1,src,dest,aux)
    tower_of_honai(1,src,aux,dest)    
    tower_of_honai(n-1,aux,src,dest)

def main():
   tower_of_honai(4,'A','B','C')

main()