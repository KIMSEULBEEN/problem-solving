"""
BOJ 2581 소수
에라토스테네스의 체
"""

import math

N = int(input())
M = int(input())

M_sqrt = int(math.sqrt(M))

numbers = [True] * (M + 1)

for num in range(2, M_sqrt + 2):
    div = N // num
    while num * div <= M:
        if div > 1:
            idx = num * div
            numbers[idx] = False
        div += 1
numbers[1] = False

answer = 0
answer_min = -1
for num in range(N, M + 1):
    if numbers[num]:
        if answer_min == -1:
            answer_min = num
        answer += num

if answer_min != -1:
    print(answer)
print(answer_min)