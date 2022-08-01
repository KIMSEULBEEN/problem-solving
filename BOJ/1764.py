"""
BOJ 1764 듣보잡
"""
import sys
input = sys.stdin.readline

names = []
N, M = list(map(int, input().split()))

for _ in range(N):
    names.append(input().rstrip())
names = set(names)

answers = []
for _ in range(M):
    name = input().rstrip()
    if name in names:
        answers.append(name)
print(len(answers))
for answer in sorted(answers):
    print(answer)