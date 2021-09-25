# 0. 입력 받기

# N, D, K 입력
N, D, K = list(map(int, input().split(' ')))
"""
N: 학생 수 [1, 1000]
D: 알고리즘 문제의 종류 [1, 15]
K: A조 학생들이 풀 수 있는 서로 다른 문제들의 총 가짓수 [1, D]

-> A조가 최대 몇명까지 가능할 수 있는가?
"""
# print(N, D, K)

# 학생 수 입력
student_info_list_ori = []
student_info_list = []
"""
N명의 학생 수에 대해서 풀 수 있는 서로 다른 문제를 입력받는다
문제의 갯수가 저장된 첫 번째 인덱스를 제외한 두 번째 인덱스부터 student_info_list에 추가한다
student_info[0] : 풀 수 있는 문제의 갯수
student_info[1] : 해당 학생이 풀 수 있는 문제의 전체/일부를 풀 수 있는 학생들의 수

student_info[1]에 학생이 추가될 경우, 해당 학생의 student_info는 [[-1], -1]로 수정된다
"""
for _ in range(N):
    student_info = list(map(int, input().split(' ')))[1:] # [2, 1]
    student_info = [student_info, 1] # [[2, 1], 2]
    student_info_list_ori.append(student_info)

student_info_list_ori.sort(key=lambda x: len(x[0]))
# print(student_info_list_ori)
answer_bias = 0

answer = 0
len_answer = 0
for student_info in student_info_list_ori:
    # student_info = list(map(int, input().split(' ')))[1:] # [2, 1]
    # student_info = [student_info, 1] # [[2, 1], 2]

    if len(student_info[0]) == 0:
        answer_bias += 1

    elif len(student_info[0]) <= K: # 해당 학생이 풀 수 있는 문제 가짓수가 K보다 작거나 같을 경우
        for idx, student_info2 in enumerate(student_info_list):
            if set(student_info2[0]).issubset(set(student_info[0])):
                if len(student_info2[0]) == len(student_info[0]):
                    student_info[1] = student_info2[1] + 1
                else:
                    student_info[1] += student_info2[1]
                student_info_list[idx] = [[-1], -1]
        # print(student_info)
        if student_info[1] > answer:
            answer = student_info[1]
            len_answer = len(student_info[0])
        student_info_list.append(student_info)



# 합계 길이가 적을 경우 다시 연산한다

# print(student_info_list)
if len_answer < K:
    student_info_list.sort(key=lambda x: len(x[0]))
    answer = 0
    answer_list = []
    len_answer = 0
    for student_info in student_info_list:
        if len(student_info[0]) > K: break

        if -1 not in student_info[0] and len_answer + len(student_info[0]) <= K:
            answer += student_info[1]
            len_answer += len(student_info[0])
            answer_list.extend(student_info[0])
            answer_list = sorted(answer_list)

        else:
            index_end = min(len(answer_list), len(student_info[0]))
            sum_answer = sum(answer_list[:index_end])
            if sum_answer < student_info[1]:
                answer -= sum_answer
                answer += student_info[1]
                answer_list = answer_list[index_end:]
                answer_list.extend(student_info[0])


# print(student_info_list)
# print(answer, len_answer)
# [[[-1], -1], [[-1], -1], [[-1], -1], [[3], 1], [[-1], -1], [[2, 1], 5]]
print(answer + answer_bias)
