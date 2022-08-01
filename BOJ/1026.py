"""
BOJ 1026 보물
"""

loops = int(input())

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

answer = 0
for idx in range(loops):
    answer += A[idx] * B[loops - idx - 1]

print(answer)

