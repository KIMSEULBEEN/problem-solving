M,N = input().split(' ')
M,N = int(M),int(N)


if N == 0: result = 1

else:
    k = 1
    result = M
    while N > 1:
        result *= (M-k)
        result /= k
        k += 1
        N -= 1
    result /= k


print(int(result))
