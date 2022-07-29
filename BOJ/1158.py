"""
BOJ 1158 요세푸스 문제
"""

N, K = list(map(int, input().split(' ')))
numbers = [n for n in range(1, N + 1)]

idx = 0
answers = []
while len(numbers) > 0:
    idx += K - 1
    idx %= len(numbers)
    answers.append(str(numbers.pop(idx)))
    # print(numbers.pop(idx))

print("<{}>".format(", ".join(answers)))