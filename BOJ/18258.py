"""
BOJ 18258 큐 2
"""
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
deq = deque([])

for _ in range(N):
    commands = input().rstrip().split()
    com = commands[0]

    if com == "push":
        deq.append(int(commands[1]))
    elif com == "pop":
        print(deq.popleft() if len(deq) > 0 else -1)
    elif com == "size":
        print(len(deq))
    elif com == "empty":
        print(1 if len(deq) == 0 else 0)
    elif com == "front":
        print(deq[0] if len(deq) > 0 else -1)
    elif com == "back":
        print(deq[-1] if len(deq) > 0 else -1)





