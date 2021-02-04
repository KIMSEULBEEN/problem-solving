numList = []
for n in range(8):
    numList.append(int(input()))

numList = list(zip(numList,list(range(1,9))))

numList = sorted(numList,key=lambda x:x[0])
numList = numList[-5:]

idxList = []
sum = 0
for num,idx in numList:
    idxList.append(idx)
    sum += num

idxList = sorted(idxList)
print(sum)
for num in idxList: print(num,end = ' ')
