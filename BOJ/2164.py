"""
BOJ 2164 카드 2
"""

from collections import deque

N = int(input())
numbers = deque([n for n in range(1, N + 1)])

while len(numbers) > 1:
    numbers.popleft()
    if len(numbers) == 1:
        break
    numbers.append(numbers.popleft())
    # print(numbers)

print(numbers[0])