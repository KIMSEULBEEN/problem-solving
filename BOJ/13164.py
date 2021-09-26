"""
입력
N: 원생의 수 [1, 300,000]
K: 조의 갯수 [1, N]

students: 학생 키 배열
"""
N, K = list(map(int, input().split(' ')))
students = list(map(int, input().split(' ')))

distances_dict = dict()
for idx in range(N - 1):
    distances_dict[idx] = students[idx + 1] - students[idx]

if K == 1:
    answer = students[-1] - students[0]

else:
    distances = sorted(distances_dict.items(), key=lambda x: x[1], reverse=True)[:K - 1]
    distances = sorted(distances, key=lambda x:x[0]) # [(0, 2), (3, 4)]
    print(distances)

    answer = 0
    for idx in range(len(distances)):
        if idx == 0:
            idx_start, idx_end = 0, distances[idx][0]
            answer += students[idx_end] - students[idx_start]

        else:
            idx_start, idx_end = distances[idx - 1][0] + 1, distances[idx][0]
            answer += students[idx_end] - students[idx_start]
    answer += students[-1] - students[idx_end + 1]

print(answer)
