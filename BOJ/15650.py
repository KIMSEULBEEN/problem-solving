from itertools import combinations

N,M = map(int,input().split(' '))


nums = list(range(1,N+1))
for comb in list(combinations(nums,M)):
    for n in comb:
        print(n,end=' ')
    print()
