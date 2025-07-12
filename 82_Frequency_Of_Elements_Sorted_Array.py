from typing import Counter


def frequency(a):
    if not a:
        return

    freq = 1
    for i in range(1, len(a)):
        if a[i] == a[i - 1]:
            freq += 1
        else:
            print(f'{a[i - 1]} {freq}')
            freq = 1

    # Always print the last group
    print(f'{a[-1]} {freq}')

def counter_build(a):
    result = Counter(a)
    for i in result:
        print(f'{i} {result[i]}')
        
def main():
    a = [20, 20, 30, 30, 1, 30]
    #a = [10]
    #frequency(a)
    counter_build(a)
main()
