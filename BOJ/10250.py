repeat = int(input())

for n in range(repeat):
    H,W,N = input().split()
    H = int(H)
    W = int(W)
    N = int(N)


    X = str(int(N%H))
    if X == '0':
        X = str(H)
    Y = str(int((N-1)/H) + 1)

    if int(Y) < 10:
        Y = '0' + Y


    print(int(X+Y))
