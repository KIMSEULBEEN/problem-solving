"""
백준 18112번 이진수 게임

입력
num: 110 (길이 [1, 10])
num_final: 1000 (길이 [1, 10])

출력
answer: 2 (num에서 num_final로 가기 위한 최소 연산)

예시
1000
11
4

110
1000
2

101
111
2


11011
10111
2

110111
111001
2

1110000000
1110011111
2
"""

# 0. 입력 받기
num = int(input(), 2) # 111
num_final = int(input(), 2)

answer = 0


# 1. num과 num_final의 길이가 다를 경우
if len(format(num, 'b')) != len(format(num_final, 'b')):
    num_bi = format(num, 'b')

    #  1) num보다 num_final의 길이가 클 경우
    #  num       100
    #  num_final 111111


    #  num 1000

    if len(format(num, 'b')) < len(format(num_final, 'b')):
        # 맨 앞 숫자를 제외한 모든 수가 1인 이진수를 만든다
        for idx in range(1, len(num_bi)):
            if num_bi[idx] != '1':
                answer += 1
        #  num -> 111


        # 자릿수 업그레이드를 위한 1 추가
        answer += 1
        #  num + 1
        #  num -> 1000       (자릿수 4개)

        # 100000
        #  num_final 111111  (자릿수 6개)

        # 남은 자릿수 크기들만큼 더해주기
        answer += sum(range(len(format(num, 'b')) + 1, len(format(num_final, 'b'))))
        #  answer = answer + 4 + 5
        #  num -> 100000

        # 자릿수 크기만큼 num 값 조정
        num = int('1' + '0' * (len(format(num_final, 'b')) - 1), 2)
        #  num -> 100000


    #  2) num보다 num_final의 길이가 작을 경우
    elif len(format(num, 'b')) > len(format(num_final, 'b')):
        # 맨 앞 숫자를 제외한 모든 수가 0인 이진수를 만든다
        for idx in range(1, len(num_bi)):
            if num_bi[idx] != '0':
                answer += 1

        # 자릿수 다운그레이드를 위한 1 추가
        answer += 1

        # 남은 자릿수 크기들만큼 더해주기
        # answer += sum(range(len(format(num, 'b')) + 1, len(format(num_final, 'b'))))
        answer += sum(range(len(format(num_final, 'b')) + 1, len(format(num, 'b'))))


        # 자릿수 크기만큼 num 값 조정
        num = int('1' + '1' * (len(format(num_final, 'b')) - 1), 2)


# 2. 보수 연산의 연산량과 함 & 차 연산의 연산량 중 적은 연산량을 적용

# 보수 연산
num_bi = format(num, 'b')
num_final_bi = format(num_final, 'b')

answer_add_1 = 0
for idx in range(1, len(num_bi)):
    if num_bi[idx] != num_final_bi[idx]:
        answer_add_1 += 1


# 합 & 차연산
answer_add_2 = abs(num - num_final)

# 더 적은 연산량 적용
answer += min(answer_add_1, answer_add_2)

print(answer_add_1, answer_add_2)
print(answer)

"""
1110000000
1110011111
"""