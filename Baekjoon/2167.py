import sys

H, W = map(int, sys.stdin.readline().split())

array = []
for n in range(H):
    array.append(list(map(int, sys.stdin.readline().split())))

dp = [[0]* W for n in range(H)]
for h in range(H):
    for w in range(W):
        if h == 0: dp[h][w] = sum(array[h][:w+1])
        else: dp[h][w] = sum(array[h][:w+1]) + dp[h-1][w]


answer = []
K = int(input())
for n in range(K):
    h1, w1, h2, w2 = map(int, sys.stdin.readline().split())
    h1, w1, h2, w2 = h1-1, w1-1, h2-1, w2-1


    if h1 == h2 and w1 == w2: _answer = array[h1][w1]
    else:
        _answer = dp[h2][w2]

        if h1 > 0: _answer -= dp[h1-1][w2]
        if w1 > 0: _answer -= dp[h2][w1-1]
        if h1 > 0 and w1 > 0: _answer += dp[h1-1][w1-1]

    answer.append(_answer)


for n in range(K): print(answer[n])
