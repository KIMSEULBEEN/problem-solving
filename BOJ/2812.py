from collections import deque
# Test
# 0. 입력 받기
len_numbers, len_numbers2 = list(map(int, input().split(' ')))
# 두 수의 길이로 입력을 받기 때문에 len_number2 값을 재조정
len_numbers2 = len_numbers - len_numbers2

numbers = deque(list(input()))
numbers2 = deque()


for idx, num in enumerate(numbers):
    len_numbers2_tmp = len(numbers2)
    # case 1. numbers2 길이가 0 일때
    if len_numbers2_tmp == 0:
        numbers2.append(num)

    else:
        idx_left = len_numbers - idx
        idx_left2 = len_numbers2 - len_numbers2_tmp

        # case 2-1. numbers 남은 숫자가 채워야할 numbers2 숫자보다 많은 경우
        if idx_left > idx_left2:
            idx_tmp = -1
            while idx_left > idx_left2 and len(numbers2) > 0 and num > numbers2[-1]:
                numbers2.pop()
                idx_left2 += 1
            numbers2.append(num)


        else:
            numbers2.append(num)

while len_numbers2 < len(numbers2): numbers2.pop()

    # print(num, numbers2)


print(''.join(numbers2))
