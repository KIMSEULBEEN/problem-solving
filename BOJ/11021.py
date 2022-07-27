"""
BOJ 11021 A + B - 7

"""

loops = int(input())

answers = []
for idx in range(loops):
    a, b = list(map(int, input().split(' ')))
    answer = "Case #{}: {}".format(idx + 1, a + b)
    answers.append(answer)

print("\n".join(answers))