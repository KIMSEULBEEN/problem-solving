"""
BOJ 1436 영화감독 숌
"""
N = int(input())

n = 0
num = 665
while n < N:
    num += 1
    if "666" in str(num):
        n += 1
print(num)