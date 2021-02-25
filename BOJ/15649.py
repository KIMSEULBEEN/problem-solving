from itertools import permutations

N,M = map(int,input().split(' '))


nums = list(range(1,N+1))
for comb in list(permutations(nums,M)):
    for n in comb:
        print(n,end=' ')
    print()
