"""
BOJ 11022 A+B - 8
"""

loop = int(input())

numbers = []
for _ in range(loop):
    a, b = list(map(int, input().split(' ')))
    numbers.append([a, b])

for idx, (a, b) in enumerate(numbers):
    print("Case #{}: {} + {} = {}".format(idx + 1, a, b, a + b))