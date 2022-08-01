"""
BOJ 1927 최소 힙
"""
import heapq as hq
import sys
input = sys.stdin.readline

N = int(input())

numbers = []
for _ in range(N):
    num = int(input())
    if num == 0:
        if len(numbers) == 0:
            print(0)
        else:
            print(hq.heappop(numbers))
    else:
        hq.heappush(numbers, num)

