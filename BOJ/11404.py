import sys

num_cities, num_loops = int(input()), int(input())
graph_2nd = [[sys.maxsize]*num_cities for _ in range(num_cities)]


# 1. 입력 경로 2차원 배열에 저장
def int_min1(int_str): return int(int_str) - 1
for _ in range(num_loops):
    s, e, dist = list(map(int_min1, sys.stdin.readline().split(' ')))
    graph_2nd[s][e] = min(dist + 1, graph_2nd[s][e])

# 2. 플로이드-와샬 알고리즘 적용
for m in range(num_cities):
    for s in range(num_cities):
        for e in range(num_cities):
            if s != e and graph_2nd[s][e] > graph_2nd[s][m] + graph_2nd[m][e]:
                graph_2nd[s][e] = graph_2nd[s][m] + graph_2nd[m][e]

# 3. Maximum number 0으로 변환
for s in range(num_cities):
    for e in range(num_cities):
        if graph_2nd[s][e] == sys.maxsize:
            graph_2nd[s][e] = 0

for nums in graph_2nd: print(*nums)
