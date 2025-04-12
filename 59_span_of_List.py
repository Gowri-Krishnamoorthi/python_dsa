def span_of_list(a):
    max = a[0]
    min = a[0]

    for i in range(0,len(a)):
        if a[i] > max:
           max = a[i]
        if a[i] < min:
            min = a[i]
    return max - min

def main():
    a = [10,20,40,99,6]
    print(span_of_list(a))

main()