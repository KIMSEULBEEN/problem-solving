import sys

len_numbers, len_quiz = list(map(int, sys.stdin.readline().split()))

numbers = [int(sys.stdin.readline()) for _ in range(len_numbers)]
quiz = [list(map(int, sys.stdin.readline().split())) for _ in range(len_quiz)]

for idx_s, idx_e in quiz:
    number_min, number_max = min(numbers[idx_s - 1:idx_e]), max(numbers[idx_s - 1:idx_e])
    print("{} {}".format(number_min, number_max))

# print(numbers)
# print(quiz)