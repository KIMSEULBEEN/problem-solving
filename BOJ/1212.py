"""
BOJ 1212 8진수 2진수
"""

number_8th = input().rstrip()

answer = ""

if number_8th == '0':
    answer = '0'
else:
    for idx, num in enumerate(number_8th):
        add = ''
        if num == '0':
            add = '000'
        elif num == '1':
            add = '001'
        elif num == '2':
            add = '010'
        elif num == '3':
            add = '011'
        elif num == '4':
            add = '100'
        elif num == '5':
            add = '101'
        elif num == '6':
            add = '110'
        elif num == '7':
            add = '111'

        if idx == 0:
            idx2 = 0
            while add[idx2] == '0':
                idx2 += 1
            add = add[idx2:]
        answer += add

print(answer)