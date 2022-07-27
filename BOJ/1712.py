"""
BOJ 1712 손익분기점

"""

A, B, C = list(map(int, input().split(' ')))

margin = C - B
if margin > 0:
    answer = A // margin + 1
    print(answer)
else:
    print(-1)