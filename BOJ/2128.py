import sys

# 0. 입력 받기

# N, D, K 입력
"""
N: 학생 수 [1, 1000]
D: 알고리즘 문제의 종류 [1, 15]
K: A조 학생들이 풀 수 있는 서로 다른 문제들의 총 가짓수 [1, D]

-> A조가 최대 몇명까지 가능할 수 있는가?
N, D, K = list(map(int, input().split(' ')))
"""
N, D, K = list(map(int, input().split(' ')))




# student_info_list

"""
student_info = [[1, 3, 5], 3]

student_info[0]: [1, 3, 5] -> 풀이 가능한 문제 갯수
student_info[1]: 3         -> 포함 인원수
"""
answer, answer_bias = 0, 0

student_info_list = []
for _ in range(N):
    student_info_cpr1 = [list(map(int, sys.stdin.readline().rstrip().split(' ')))[1:], 1]
    if len(student_info_cpr1[0]) > K:
        continue

    if len(student_info_cpr1[0]) == 0:
        answer_bias += 1

    elif len(student_info_list) == 0:
        answer = 1
        student_info_list.append(student_info_cpr1)

    else:
        # print(student_info_cpr1, student_info_list)
        student_info_list_tmp = []
        for student_info_cpr2 in student_info_list:
            num_problems = len(list(set(student_info_cpr1[0] + student_info_cpr2[0])))
            if num_problems <= K:
                student_info_cpr3 = [list(set(student_info_cpr1[0] + student_info_cpr2[0]))
                                        ,student_info_cpr1[1] + student_info_cpr2[1]]
                student_info_list_tmp.append(student_info_cpr3)
                # print('good', student_info_cpr3)
            else:
                student_info_cpr3 = student_info_cpr2

            answer = max(answer, student_info_cpr3[1])


        student_info_list.append(student_info_cpr1)
        student_info_list.extend(student_info_list_tmp)

        student_info_list_tmp = []

        problems_prev = []
        persons_prev = 0
        for student_info in student_info_list:
            problems_cpr = student_info[0]
            persons_cpr = student_info[1]

            if problems_cpr == problems_prev:
                problems_cpr = max(problems_cpr, problems_prev)

            else:
                if persons_prev > 0:
                    student_info_list_tmp.append([problems_prev, persons_prev])

            problems_prev = problems_cpr
            persons_prev = persons_cpr
        student_info_list_tmp.append([problems_prev, persons_prev])
        student_info_list = student_info_list_tmp

print(answer + answer_bias)


