"""
BOJ 10950 A+B-3
"""

loops = int(input())

numbers = []
for _ in range(loops):
    a, b = list(map(int, input().split(' ')))
    numbers.append(str(a + b))

print("\n".join(numbers))