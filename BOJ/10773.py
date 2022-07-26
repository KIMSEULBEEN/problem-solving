import sys

input = sys.stdin.readline

K = int(input())
stack = []

answer = 0
for _ in range(K):
    n = input().rstrip()
    if n == '0':
        answer -= stack.pop()
    else:
        n = int(n)
        stack.append(n)
        answer += n

print(answer)
