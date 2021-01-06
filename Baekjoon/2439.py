N = int(input())

num = 1

for n in range(N):
    blanknum = 0
    for m in range(num):
        if blanknum == 0:
            for k in range(N-num):
                print(' ',end='')
        print('*',end='')
        blanknum = 1
    num+=1
    print()
