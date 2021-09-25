import sys

# 0. 입력 받기

# N, D, K 입력
"""
N: 학생 수 [1, 1000]
D: 알고리즘 문제의 종류 [1, 15]
K: A조 학생들이 풀 수 있는 서로 다른 문제들의 총 가짓수 [1, D]

-> A조가 최대 몇명까지 가능할 수 있는가?
"""
N, D, K = list(map(int, input().split(' ')))


# student_info_list
"""
student_info = [3, [1, 3, 5], 4]

student_info[0]: 3         -> 풀이 가능한 문제 갯수
student_info[1]: [1, 3, 5] -> 풀이 가능한 문제 종류
student_info[2]: 4         -> 포함 인원수
"""
answer, answer_bias = 0, 0

student_info_list = []
for _ in range(N):
    student_info_cpr1 = sys.stdin.readline().rstrip().split(' ')
    student_info_cpr1 = [int(student_info_cpr1[0]), sorted(student_info_cpr1[1:]), 1]
    if student_info_cpr1[0] > K:
        continue

    if student_info_cpr1[0] == 0:
        answer_bias += 1

    elif len(student_info_list) == 0:
        answer = 1
        student_info_list.append(student_info_cpr1)

    else:
        # print(student_info_cpr1, student_info_list)
        student_info_list_tmp = []
        for student_info_cpr2 in student_info_list:
            # print(student_info_cpr2)
            problems = list(set(student_info_cpr1[1] + student_info_cpr2[1]))
            num_problems = len(problems)
            if num_problems > K:
                student_info_cpr3 = student_info_cpr2
            else:
                student_info_cpr3 = [num_problems, problems, student_info_cpr1[2] + student_info_cpr2[2]]
                student_info_list_tmp.append(student_info_cpr3)
                # print('good', student_info_cpr3)

        student_info_list.append(student_info_cpr1)
        student_info_list.extend(student_info_list_tmp)
        student_info_list = sorted(student_info_list, key=lambda x: x[0])

        student_info_list_tmp = []
        problems_prev = []
        persons_prev = 0
        for student_info in student_info_list:
            num_problems_cpr = student_info[0]
            problems_cpr = student_info[1]
            persons_cpr = student_info[2]

            if problems_cpr == problems_prev:
                num_problems_cpr = max(num_problems_cpr, num_problems_prev)

            else:
                if persons_prev > 0:
                    student_info_list_tmp.append([num_problems_prev, problems_prev, persons_prev])

            num_problems_prev = num_problems_cpr
            problems_prev = problems_cpr
            persons_prev = persons_cpr
        student_info_list_tmp.append([num_problems_prev, problems_prev, persons_prev])
        student_info_list = student_info_list_tmp
        # print(student_info_list)

answer = 0
for student_info in student_info_list:
    answer = max(answer, student_info[2])


print(answer + answer_bias)


