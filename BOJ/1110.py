n_ori = int(input())

n = -1
cnt = 0
while n != n_ori:
    if n == -1:
        n = n_ori

    n_10 = int(n/10)
    n_1 = int(n%10)

    n_new1 = int((n_10 + n_1)%10)

    n = 10*n_1 + n_new1

    cnt += 1

print(cnt)
