"""
BOJ 10953 A + B - 6
"""
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = list(map(int, input().split(',')))
    print(a + b)