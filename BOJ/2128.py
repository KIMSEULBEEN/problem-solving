
import sys
"""
N: 학생 수 [1, 1000]
D: 알고리즘 문제의 종류 [1, 15]
K: A조 학생들이 풀 수 있는 서로 다른 문제들의 총 가짓수 [1, D]

-> A조가 최대 몇명까지 가능할 수 있는가?
"""
N, D, K = list(map(int, input().split(' ')))
student_info_list = []
for _ in range(N):
    student_info = list(map(int, sys.stdin.readline().rstrip().split(' ')))[1:]
    student_info_list.append(student_info)


from itertools import combinations
combs = list(combinations(range(1, D + 1), K))

answer = 0
for student_info in combs:
    answer_tmp = 0
    for student_info_cpr in student_info_list:
        if len(student_info_cpr) == 0:
            answer_tmp += 1

        elif set(student_info_cpr).issubset(set(student_info)):
            answer_tmp += 1
    answer = max(answer, answer_tmp)
print(answer)



