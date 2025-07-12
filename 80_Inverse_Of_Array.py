def inverse(a):
    # b = [0] * len(a)

    # for i in range(len(a)):
    #     v = a[i]
    #     if v < len(a):
    #         b[v] = i
    # return b

    #for clarification
    # a = [2, 0, 3, 1]
    # n = len(a) = 4
    # sorted(a) = [0, 1, 2, 3]
    # list(range(n)) = [0, 1, 2, 3]

    n = len(a)
    if sorted(a) != list(range(n)):
        raise ValueError("Input must be a permutation of 0 to n-1.")
    
    b = [0] * n
    for i in range(n):
        v = a[i]
        b[v] = i
    return b

def main():
    a = [2,3,1,0,7]
    b = inverse(a)
    print(a)
    print(b)
main()