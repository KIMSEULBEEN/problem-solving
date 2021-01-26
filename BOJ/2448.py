def blankarr(width,height):
    tmp = []
    bl = ''
    for w in range(width):
        bl += ' '

    for h in range(height):
        tmp.append(bl)

    return tmp

def insertarr(tmp,arr,y,x):
    width,height = int(len(arr[0])),int(len(arr))

    for h in range(height):
        tmp[y+h] = tmp[y+h][:x] + arr[h] + tmp[y][x+width:]

    return tmp

def arrup(arr):
    width,height = int(len(arr[0])),int(len(arr))

    tmp = blankarr(2*width+1,2*height)

    tmp = insertarr(tmp,arr,0,height)
    tmp = insertarr(tmp,arr,height,0)
    tmp = insertarr(tmp,arr,height,2*height)

    return tmp

def printarr(arr):
    height = len(arr)

    for h in range(height):
        print(arr[h])

N = int(input())
N = int(N/3)

num = 0
while N >= 1:
    N = N/2
    num+=1

arr = ['  *  ',' * * ','*****']

for n in range(num):
    if n == 0:
        tmp = arr
    else:
        tmp = arrup(tmp)

printarr(tmp)

