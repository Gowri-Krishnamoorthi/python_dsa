def reverse_string(s,r,i):
    if i < 0:
        return r

    return reverse_string(s, r + s[i] , i-1)

s = input("Enter a String \n")
print(reverse_string(s,"",len(s)-1))