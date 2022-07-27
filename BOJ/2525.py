"""
BOJ 2525 오븐 시계
"""

hour, min = list(map(int, input().split(' ')))
min_plus = int(input())

min += min_plus
hour += min // 60
hour %= 24
min %= 60

print("{} {}".format(hour, min))