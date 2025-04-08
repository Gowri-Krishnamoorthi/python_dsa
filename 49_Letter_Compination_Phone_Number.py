keypad = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

def possible_words(s, ans):

    if len(s) == 0:
        print(ans)
        return
    
    key = keypad[ int(s[0]) ]

    for i in key:
        possible_words(s[1:] , ans+i)

def main():
    s = input("Enter a value \n")
    possible_words(s,'')

main()