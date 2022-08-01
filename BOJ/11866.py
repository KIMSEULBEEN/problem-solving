"""
BOJ 11866 요세푸스 문제 0
"""

N, K = list(map(int, input().split()))

numbers = [n for n in range(1, N + 1)]
answers = []

idx = 0
while len(numbers) > 0:
    idx += K - 1
    idx %= len(numbers)
    answers.append(str(numbers.pop(idx)))

print("<{}>".format(", ".join(answers)))