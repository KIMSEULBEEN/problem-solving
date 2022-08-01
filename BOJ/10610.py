"""
BOJ 10610 30
"""

number = input().rstrip()
numbers_str = list(number)
numbers = list(map(int,list(number)))


if sum(numbers) % 3 != 0 or '0' not in number:
    print(-1)
else:
    print(''.join(sorted(numbers_str, reverse=True)))
