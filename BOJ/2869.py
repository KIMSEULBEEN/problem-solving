"""
BOJ 2869 달팽이는 올라가고 싶다
"""

A, B, V = list(map(int, input().split(' ')))
day = A - B


answer = (V - A) // day
height = day * answer
while height < V:
    answer += 1
    height += A

    if height >= V:
        break
    else:
        height -= B
print(answer)