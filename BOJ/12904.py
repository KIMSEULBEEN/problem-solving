from collections import deque

# 0. 문자열 S와 T입력으로 받는다
str_s = input()
str_t = input()
deque_t = deque(str_t)

# 1. deque_t의 길이가 str_s의 길이와 같아질 때까지 pop
len_str_s = len(str_s)
while len_str_s < len(deque_t):
    chr_tmp = deque_t.pop()
    if chr_tmp == 'B':
        deque_t.reverse()

# 2. str_s와 str_t가 같으면 1 다르면 0을 출력한다.
str_t = ''.join(deque_t)

if str_s == str_t: print(1)
else: print(0)
