lst = []

def possible_combinations(s, ans):
    if len(s) == 0:
        #print(ans)
        lst.append(ans)
        return
    
    possible_combinations(s[1:] , ans+s[0])
    possible_combinations(s[1:], ans)

def main():
    s = input()
    possible_combinations(s,'')
    print(lst)
main()