"""
N: 선물 주문의 갯수 [1, 100,000]
K: 생산 라인의 갯수
X: 제작 완료까지 남은 시간 [1, 10^9]

gifts: 선물 별 제작 시간 리스트
"""
N, X = list(map(int, input().split(' ')))
times = list(map(int, input().split(' ')))

import heapq as hq

def check_possibility(K):
    assembly_lines = [0] * K
    hq.heapify(assembly_lines)

    for time in times:
        time_sum = hq.heappop(assembly_lines) + time
        hq.heappush(assembly_lines, time_sum)
        if time_sum > X: return False
    return True

if len(times) == 1:
    print(1)

else:
    low = 1
    high = len(times)
    is_possible = False
    while low <= high:
        mid = (low + high) // 2

        is_possible = check_possibility(mid)
        if is_possible:
            high = mid - 1
        else:
            low = mid + 1

    if is_possible:
        print(mid)
    else:
        print(mid + 1)