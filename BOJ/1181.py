import sys

readline = lambda: sys.stdin.readline()
num = int(readline())
A = []
for n in range(num):
    A.append(readline())

A = sorted(list(set(A)))


A_s = [[] for i in range(100)] # 50*0

for a in A:
    A_s[len(a)].append(a)



for a in A_s:
    for n in range(len(a)):
        print(a[n],end='')






