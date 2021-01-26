N = int(input())

num = N

for n in range(N):
    blanknum = 0
    for m in range(num):
        if m == 0:
            for k in range(N-num):
                print(' ',end='')
        print('*',end='')

    num -= 1
    print()
