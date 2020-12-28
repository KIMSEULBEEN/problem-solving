def num_comb(a, b):
    max_ab, min_ab = max(a, b), min(a, b)

    bunza = max_ab
    for n in range(1, min_ab):
        bunza *= (max_ab - n)

    bunmo = 1
    for n in range(2, min_ab + 1): bunmo *= n

    return bunza // bunmo

num_loop = int(input())


ANSWER = []
for num in range(num_loop):
    a, b = list(map(int, input().split(' ')))
    ANSWER.append(num_comb(a, b))

for answer in ANSWER: print(answer)
