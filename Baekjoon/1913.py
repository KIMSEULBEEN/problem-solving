lenMatrix = int(input())
numSearch = int(input())

Matrix = [[0] * lenMatrix for _ in range(lenMatrix)]


def fill_matrix(lenMatrix, sIdx, numSearch):
    xT, yT = -1, -1

    if lenMatrix == 1:
        Matrix[sIdx][sIdx] = 1
        if numSearch == 1: xT, yT = sIdx, sIdx

    else:
        num = lenMatrix ** 2
        for y in range(lenMatrix - 1):
            Matrix[y + sIdx][0 + sIdx] = num
            if num == numSearch: xT, yT = 0 + sIdx, y + sIdx
            num -= 1


        for x in range(lenMatrix - 1):
            Matrix[lenMatrix - 1 + sIdx][x + sIdx] = num
            if num == numSearch: xT, yT = x + sIdx, lenMatrix - 1 + sIdx
            num -= 1


        for y in range(lenMatrix -1, 0, -1):
            Matrix[y + sIdx][lenMatrix - 1 + sIdx] = num
            if num == numSearch: xT, yT = lenMatrix - 1 + sIdx, y + sIdx
            num -= 1


        for x in range(lenMatrix - 1, 0, -1):
            Matrix[0 + sIdx][x + sIdx] = num
            if num == numSearch: xT, yT = x + sIdx, 0 + sIdx
            num -= 1
    # print(lenMatrix, x, y, numSearch)
    return xT, yT


cnt = 0
x, y = -1, -1
for lenMatrixTmp in range(lenMatrix, 0, -2):
    xT, yT = fill_matrix(lenMatrixTmp, cnt, numSearch)
    # print(x, y)
    if xT != -1: x, y = xT, yT
    cnt += 1


for n in range(lenMatrix):
    for m in range(lenMatrix): print(Matrix[n][m], end = ' ')
    print()

print(str(y+1) + ' ' + str(x+1))
