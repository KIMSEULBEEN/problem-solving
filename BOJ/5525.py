N = int(input())
len_S = int(input())
S = input()

answer, idx = 0, 0

s_prev = 'O'
count_i = 0
while idx < len(S):
    s = S[idx]
    if s == 'I':
        if s_prev == 'O': # 'OI'
            count_i += 1

        else: # 'II'
            if count_i > N:
                answer += count_i - N
            count_i = 1

    else: # 'O'
        if s_prev == 'O': # '00'
            if count_i > N:
                answer += count_i - N
            count_i = 0

        else: # 'I0'
            pass

    s_prev, idx = s, idx + 1

if count_i > N:
    answer += count_i - N

print(answer)
