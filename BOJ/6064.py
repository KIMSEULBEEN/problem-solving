for k in range(int(input())):
    M,N,x,y = input().split()

    M = int(M)
    N = int(N)
    x = int(x)
    y = int(y)

    maxnum = M*N

    num = x


    while num<=maxnum:
        
        if y%N == num%N:
            print(num)
            break
        num += M


    if num>maxnum:
        print(-1)
