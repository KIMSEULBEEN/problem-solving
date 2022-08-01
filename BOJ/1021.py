"""
BOJ 1021 회전하는 큐
"""
from collections import deque

N, M = list(map(int, input().split()))

numbers = deque([n for n in range(1, N + 1)])
numbers_test = list(map(int, input().split()))

answer = 0
for num in numbers_test:
    idx = numbers.index(num)
    if idx != 0:
        idx_left = idx
        idx_right = abs(idx - len(numbers))

        if idx_left < idx_right:
            for _ in range(idx_left):
                answer += 1
                numbers.append(numbers.popleft())
        else:
            for _ in range(idx_right):
                answer += 1
                numbers.appendleft(numbers.pop())

    numbers.popleft()
print(answer)