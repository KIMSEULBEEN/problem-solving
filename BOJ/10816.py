"""
BOJ 10816 숫자 카드 2
"""

import sys
input = sys.stdin.readline

numbers = dict()

input()
numbers_input = list(map(int, input().split(' ')))
for n in numbers_input:
    if n in numbers.keys():
        numbers[n] += 1
    else:
        numbers[n] = 1
    # print(n, numbers, numbers_input)

input()
numbers_check = list(map(int, input().split()))
for n in numbers_check:
    if n in numbers.keys():
        print(numbers[n], end = ' ')
    else:
        print('0', end = ' ')
print()