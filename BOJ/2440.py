N = int(input())

num = N

for n in range(N):
    for m in range(num):
        print('*',end='')

    num -= 1
    print()
