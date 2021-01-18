N = int(input())

arrN = set(input().split(' '))

M = int(input())

arrM = list(input().split(' '))


for num in arrM:
    if num in arrN: print(1)
    else: print(0)
        
