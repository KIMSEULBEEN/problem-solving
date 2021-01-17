import sys

readline = lambda: sys.stdin.readline()
N = sorted(readline())

len_N = len(N)

for n in range(len_N):
    print(N.pop(),end='')

