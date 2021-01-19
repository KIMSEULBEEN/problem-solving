import sys


def sosu(num):
    if num == 1:
        return False

    for n in range(2,num):
        if int(num%n) == 0:
            return False
    return True


readline = lambda: sys.stdin.readline()
N = int(readline())

num_sosu = 0

A = input().split()

for num in A:
    num = int(num)
    if sosu(num) == True:
        num_sosu+=1

print(num_sosu)
