"""
백준 알고리즘 11286번
절댓값 힙
"""
import sys
import heapq as hq


class AbsHeap:
    def __init__(self):
        self.heap_plus = []
        self.heap_minus = []

        hq.heapify(self.heap_plus)
        hq.heapify(self.heap_minus)

    def solution(self, N):
        """
        :param N: 배열의 크기
        :return:
        """

        for _ in range(N):
            num = int(sys.stdin.readline().rstrip())
            if num > 0:
                hq.heappush(self.heap_plus, num)
            elif num < 0:
                # num이 0보다 작을 경우 -를 붙인다
                hq.heappush(self.heap_minus, -num)
            else: # num == 0
                # 1. heap_plus와 heap_minus 배열 크기가 둘 다 0보다 클 경우
                if len(self.heap_plus) > 0 and len(self.heap_minus) > 0:
                    if self.heap_plus[0] < self.heap_minus[0]:
                        print(hq.heappop(self.heap_plus))
                    else:
                        print(-hq.heappop(self.heap_minus))

                # 2. heap_plus 배열 크기만 0보다 클 경우
                elif len(self.heap_plus) > 0:
                    print(hq.heappop(self.heap_plus))

                # 3. heap_minus 배열 크기만 0보다 클 경우
                elif len(self.heap_minus) > 0:
                    print(hq.heappop(self.heap_minus))

                # 4. heap_plus와 heap_minus 배열 크기가 둘 다 0일 경우
                else:
                    print(0)


abs_heap = AbsHeap()
N = int(input())
abs_heap.solution(N)