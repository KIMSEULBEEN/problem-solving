N = input()
N_int = int(N)



if N_int<100:
    print(N)

else:
    cnt = 99

    for n in range(100,N_int+1):

        n = str(n)

        n_100 = int(n[0])
        n_10 = int(n[1])
        n_1 = int(n[2])

        if n_1 - n_10 == n_10 - n_100:
            cnt += 1


    print(cnt)
