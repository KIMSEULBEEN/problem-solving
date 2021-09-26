"""
N: 선물 주문의 갯수 [1, 100,000]
K: 생산 라인의 갯수
X: 제작 완료까지 남은 시간 [1, 10^9]

gifts: 선물 별 제작 시간 리스트
"""
N, X = list(map(int, input().split(' ')))
gifts = list(map(int, input().split(' ')))

import heapq as hq

def check_possibility(K):
    assembly_lines = [0] * K
    hq.heapify(assembly_lines)

    for gift in gifts:
        time = hq.heapify(assembly_lines) + gift
        if time > X: return False
    return True

start = 0
end = len(gifts)
mid = (start + end) // 2

is_produce = False
while is_produce is False:
