"""
BOJ 2480 주사위 세개
"""
numbers_ori = sorted(list(map(int, input().split(' '))))
numbers = sorted(list(set(numbers_ori)))

len_numbers = len(numbers)

# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.

answer = 0

# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
if len_numbers == 1:
    answer = 10000 + numbers[0]*1000
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
elif len_numbers == 2:
    answer = 1000 + numbers_ori[1]*100
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
elif len_numbers == 3:
    answer = numbers[-1]*100

print(answer)
