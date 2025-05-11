def leaders_in_array(a):
    # Nave Apporach
    # for i in range(len(a)):
    #     isLeader = True
    #     for j in range(i+1, len(a)):
    #         if a[j] >= a[i] :
    #             isLeader = False
    #             break
    #     if isLeader == True:
    #         print(a[i])

    current_leader = a[len(a)-1]
    print(current_leader)

    for i in range(len(a)-2, -1, -1):
        if a[i] > current_leader:
            current_leader = a[i]
            print(current_leader)

def main():
    a = [8,11,5,11,7,6,3]
    leaders_in_array(a)
main()