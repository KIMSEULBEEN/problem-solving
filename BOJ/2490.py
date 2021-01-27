yutList = ['E','A','B','C','D']

yutArr = []
for n in range(3):
    inputList = list(map(int,input().split(' ')))
    yutArr.append(yutList[inputList.count(0)])

for n in range(3): print(yutArr[n])
