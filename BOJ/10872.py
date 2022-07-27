"""
BOJ 10872 팩토리얼

"""

N = int(input())

answer = 1
for n in range(1, N + 1):
    answer *= n
print(answer)