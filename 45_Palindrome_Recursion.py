def is_palindrome(s,i,j):
    if (s[i] != s[j]):
        return False
    if (j<=i):
        return True
    
    return is_palindrome(s, i+1, j-1)

s = input("Enter a String \n")
print(is_palindrome(s,0,len(s)-1))