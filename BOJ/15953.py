import sys

def first_code(num):
    ds = 0
    for n in range(1,8):
        ds += n
        if num == 0:
            break
        if num <= ds:
            break
    if num == 0:
        return 0

    if n == 1:
        return 500
    elif n == 2:
        return 300
    elif n == 3:
        return 200
    elif n == 4:
        return 50
    elif n == 5:
        return 30
    elif n == 6:
        return 10
    else:
        return 0

def second_code(num):
    ds = 0
    for n in range(6):
        ds += 2**n
        if num == 0:
            break
        if num <= ds:
            break
    n += 1
    if num == 0:
        return 0

    if n == 1:
        return 512
    elif n == 2:
        return 256
    elif n == 3:
        return 128
    elif n == 4:
        return 64
    elif n == 5:
        return 32
    else:
        return 0

readline = lambda: sys.stdin.readline()
N = int(readline())

A = []
B = []

for n in range(N):
    tmp = list(map(int,readline().split()))
    A.append(tmp[0])
    B.append(tmp[1])


for n in range(N):
    tmp = first_code(A[n]) + second_code(B[n])
    print(int(tmp*1e4))
