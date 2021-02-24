import sys
import heapq as hq

num_loop = int(input())

answers = []

if num_loop == 1:
    print(int(input()))

else:
    def int_min(int_str): return -1 * int(int_str)

    for len_answers in range(1, num_loop + 1):
        # 1. 입력 행 최대 heap 자료구조로 변환
        heap = []
        heap.extend(list(map(int_min, sys.stdin.readline().split(' '))))
        hq.heapify(heap)

        # 2. answers 최소 heap 자료구조로 변환
        hq.heapify(answers)

        while len_answers >= len(answers):
            if len(answers) > 0:
                if answers[0] < -heap[0]:
                    if len(answers) == len_answers: hq.heappop(answers)
                    hq.heappush(answers, -hq.heappop(heap))

                else: hq.heappush(answers, -hq.heappop(heap))

            else:
                hq.heappush(answers, -hq.heappop(heap))

    hq.heappop(answers)
    print(answers[0])
