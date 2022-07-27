"""
BOJ 3052 나머지

"""

answers = []
for _ in range(10):
    answers.append(int(input()) % 42)

answer = len(set(answers))
print(answer)