from collections import deque
import sys

# 입력
len_numbers = int(input())

# 양의 정수 리스트, 음의 정수 리스트
plus_numbers, minus_numbers = [], []
numbers = list(map(int, sys.stdin.readline().split(' ')))
for number in numbers:
    if number > 0:
        plus_numbers.append(number)
    else:
        minus_numbers.append(number)

plus_numbers = sorted(plus_numbers)
minus_numbers = sorted(minus_numbers, reverse=True)

"""
양의 정수 리스트의 가장 작은 두 수의 합과, 음의 정수 리스트의 가장 작은 두 수의 합 중 작은 값을 초기 answer로 취함
"""
sum_plus_2, sum_minus_2 = sum(plus_numbers[:2]), sum(minus_numbers[:2])

if len(plus_numbers) >= 2 and len(minus_numbers) >= 2:
    is_minus_low = sum_plus_2 > -sum_minus_2
    if is_minus_low:
        answer = -sum_minus_2
        answer_list = minus_numbers[:2]
    else:
        answer = sum_plus_2
        answer_list = plus_numbers[:2]

elif len(plus_numbers) >= 2:
    answer = sum_plus_2
    answer_list = plus_numbers[:2]

elif len(minus_numbers) >= 2:
    answer = sum_minus_2
    answer_list = minus_numbers[:2]

else:
    answer = sys.maxsize

if len(plus_numbers) > 0 and len(minus_numbers) > 0:
    plus_numbers, minus_numbers = deque(plus_numbers), deque(minus_numbers)
    # print(plus_numbers)
    # print(minus_numbers)
    number_plus, number_minus = plus_numbers.popleft(), minus_numbers.popleft()
    # print(number_plus, number_minus, answer)
    while abs(answer) > 0:
        answer_tmp = number_plus + number_minus
        if abs(answer_tmp) < abs(answer):
            answer = answer_tmp
            answer_list = [number_minus, number_plus]

        if number_plus < -number_minus:
            if len(plus_numbers) == 0: break
            number_plus = plus_numbers.popleft()
        else:
            if len(minus_numbers) == 0: break
            number_minus = minus_numbers.popleft()

print(*sorted(answer_list))