'''There is given an integer array A of size N denoting the heights of N tress
Lumberjack Ojas needs to chop down B metres of wood . It is an easy job for him
since he has a nifty new woodcutting machinge that can take down forests like dildfire. 
However, Ojas is only allowed to cut a single row of trees. Ojas's maching works as 
follows:
Ojas sets a height parameter H(in meters) and the machine raises a giant sawblack to that
height and cuts off all tree parts higher than H (of course, tress not higher than H)
of course , trees not higher than H meters remain in fact.Ojas then takes the parts
that were cut off. ex, if the treee row contains trees with heights of 20 , 15 , 10 and H 
meters and ojas raises his ssawblade to 15meters the reamaining treee heights after 
cutting will be 15,15,10 and 15 metres, respectively , while ojas will take 5m off the 
first tree and 2m off the fourth tree (7m of wood in total).Ojas is ecologically minded , 
so he didn't want to cut off more wood than necessary. That;s why he wants to set his 
sawblade as high as height of the sawblade that still allows him to cut off at 
least b m of wood
Note: THe sum of all heights will exceed B . thus Ojas will always be able to obtain the 
required amount of wood
'''
def find_wood_count(ht,m):
    wc = 0
    for i in ht:
        if i > m:
            wc = wc + (i-m)
    print(wc)
    return wc

def find_maxHeight(ht,b):
    #max_value = 0
    max_value = max(ht)
    # for i in ht:
    #     if max < i:
    #         max = i
    print("max",max_value)
    
    l , h, m = 0 , max_value  , 0
    
    while(l<=h):
        m = l + (h-l)//2
        wc = find_wood_count(ht,m)

        if wc == b or l == m:
            return m
        elif wc > b:
            l=m
        else:
            h=m

    return -1

def main():
    ht = [20,15,10,17]
    b = 8
    print(find_maxHeight(ht,b))

main()