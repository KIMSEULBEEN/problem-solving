"""
BOJ 1966 프린터 큐
"""
from collections import deque
loops = int(input())


for _ in range(loops):
    len_papers, idx_now = list(map(int, input().split(' ')))
    papers = deque(map(int, input().split(' ')))
    papers_bool = deque([False] * len_papers)
    papers_bool[idx_now] = True

    priority = papers[idx_now]
    answer = 0
    while True:
        # 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다
        priority_0 = papers[0]

        # 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다
        priority_max = max(papers)
        if priority_max > priority_0:
            papers.append(papers.popleft())
            papers_bool.append(papers_bool.popleft())

        # 그렇지 않다면 바로 인쇄를 한다.
        else:
            answer += 1
            papers.popleft()
            if papers_bool.popleft():
                break

    print(answer)