import sys

matrixNUM = [[] for n in range(26)]
for h in range(5):
    listNum = list(map(int, sys.stdin.readline().split()))
    for w, num in enumerate(listNum):
        matrixNUM[num] = [h, w]
# print(matrixNUM)


listNumCalled = []
for _ in range(5):
    listNum = list(map(int, sys.stdin.readline().split()))
    listNumCalled.extend(listNum)
# print(listNumCalled)



matrixBINGO = [[False] * 5 for _ in range(5)]
for num, numCalled in enumerate(listNumCalled):
    h, w = matrixNUM[numCalled]
    matrixBINGO[h][w] = True

    bingoCnt = 0
    for h in range(5):
        if False not in matrixBINGO[h]: bingoCnt += 1

    for w in range(5):
        if False not in [matrixBINGO[h][w] for h in range(5)]: bingoCnt += 1


    if False not in [matrixBINGO[n][n] for n in range(5)]: bingoCnt += 1


    if False not in [matrixBINGO[n][-n-1] for n in range(5)]: bingoCnt += 1

    if bingoCnt >= 3: break

# print()
# print([matrixBINGO[n][n] for n in range(5)])
# print([matrixBINGO[n][-n-1] for n in range(5)])
# print()
# for tmp in matrixBINGO: print(tmp+1)
# rint(matrixBINGO)
print(num+1)

