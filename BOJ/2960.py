N, K = list(map(int, input().split()))

numbers = [n for n in range(2, N + 1)]


answers = []


while len(answers) < K:
    min_numbers = min(numbers)
    number_tmp = []
    for n in numbers:
        if n % min_numbers == 0:
            answers.append(n)
            if len(answers) == K: break
        else: number_tmp.append(n)
    numbers = number_tmp

answer = answers[-1]
print(answer)
