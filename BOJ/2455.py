maxNum = 0

stNum = 0
for n in range(4):
    numout,numin = list(map(int,input().split(' ')))
    stNum = stNum + numin - numout
    if stNum > maxNum: maxNum = stNum

print(maxNum)
