"""
BOJ 1874 스택 수열
"""
from sys import stdin

# 입력
n = int(input())
numbers = [int(stdin.readline()) for _ in range(n)]

stack = []
answers = []


idx_numbers = 0
num = 1
while True:
    # stack 마지막 수와 수열의 수가 같을 경우 pop
    if len(stack) > 0 and stack[-1] == numbers[idx_numbers]:
        stack.pop()
        idx_numbers += 1
        answers.append('-')

    # 다를 경우
    else:
        # num > n일 경우 NO 출력
        if num > n:
            print("NO")
            break
        else:
            stack.append(num)
            answers.append('+')
            num += 1

    if idx_numbers == n:
        for c in answers:
            print(c)
        break

