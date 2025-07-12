# given a rope of length n , you need to find the maximum number
# of pieces you can make such that the length of every piece is in set {a,b,c}
#for the given three values a,b,c

def max_pieces(n, a, b, c):

    if (n == 0):
        return 0
    elif (n < 0) :
        return -1
    
    # temp1 = max_pieces(n-a , a, b, c)
    # temp2 = max_pieces(n-b , a, b, c)``
    # temp3 = max_pieces(n-c , a, b, c)

    # max(temp1 , temp2 , temp3)

    pieces = max(max_pieces(n-a , a, b, c) , max_pieces(n-b , a, b, c) , max_pieces(n-c , a, b, c))

    if pieces == -1:
        return -1
    
    return pieces + 1
    

def main():
    print(max_pieces(15,5,7,8))

main()


# def max_pieces(n, a, b, c):
#     if n == 0:
#         return 0, []  # base case: 0 pieces, empty path
#     elif n < 0:
#         return -1, None  # invalid path

#     # Recursive calls
#     res_a, path_a = max_pieces(n - a, a, b, c)
#     res_b, path_b = max_pieces(n - b, a, b, c)
#     res_c, path_c = max_pieces(n - c, a, b, c)

#     # Find the max among valid results
#     max_val = max(res_a, res_b, res_c)
    
#     if max_val == -1:
#         return -1, None  # no valid cut

#     # Pick the corresponding path
#     if max_val == res_a:
#         return res_a + 1, path_a + [a]
#     elif max_val == res_b:
#         return res_b + 1, path_b + [b]
#     else:
#         return res_c + 1, path_c + [c]

# def main():
#     count, cuts = max_pieces(15, 5, 8, 7)
#     print("Max pieces:", count)
#     print("Cuts used:", cuts)

# main()
