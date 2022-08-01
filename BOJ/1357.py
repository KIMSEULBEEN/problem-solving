"""
BOJ 1357 뒤집힌 덧셈
"""

X, Y = list(input().split())
XY = int(X[::-1]) + int(Y[::-1])
answer = str(XY)[::-1]

idx = 0
while answer[idx] == '0':
    idx += 1
answer = answer[idx:]

print(answer)