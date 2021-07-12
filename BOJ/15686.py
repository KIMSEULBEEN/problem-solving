import sys
from itertools import combinations

# 입력 받기
rows_cols, num_chickens = list(map(int, input().split()))
city = [list(map(int, sys.stdin.readline().split())) for _ in range(rows_cols)]

# 치킨집, 집 위치 파악
houses, chickens_total = [], []
for r in range(rows_cols):
    for c in range(rows_cols):
        if city[r][c] == 1:
            houses.append([r, c])
        elif city[r][c] == 2:
            chickens_total.append([r, c])
num_houses_total, num_chickens_total = len(houses), len(chickens_total)

# print(houses) # [[0, 2], [1, 4], [2, 1], [3, 2]]
# print(chickens_total) # [[1, 2], [2, 2], [4, 4]]


# 조합별 도시의 치킨 거리 출력
distance_total_min = 99999999

chickens_combs = combinations(chickens_total, num_chickens)
for chickens in chickens_combs:
    distance_total = 0
    for house in houses:
        r_h, c_h = house
        distance_min = 9999999
        for chicken in chickens:
            r_c, c_c = chicken
            distance = abs(r_h - r_c) + abs(c_h - c_c)
            distance_min = min(distance, distance_min)
        distance_total += distance_min
    distance_total_min = min(distance_total_min, distance_total)

print(distance_total_min)
