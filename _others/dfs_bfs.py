import sys
from collections import deque

num_nodes, num_loops, root = list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(num_nodes + 1)]

for _ in range(num_loops):
    node1, node2 = list(map(int, sys.stdin.readline().split()))
    graph[node1].append(node2)
    graph[node2].append(node1)
for n in range(num_nodes + 1): graph[n].sort()
print(graph)

def dfs(graph, root_node):
    visit, stack = [], [root_node]

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(reversed(graph[node]))
            # pop은 뒤에서부터 검출되기 때문에, 오름차순으로 graph를 생성했을 경우 반대로 넣어주어야 올바른 출력이 나온다

    for v in visit: print(v, end=' ')
    print()

    # return visit


def bfs(graph, root_node):
    visit, queue = [], deque([root_node])

    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    for v in visit: print(v, end=' ')
    print()

    # return visit


dfs(graph, root)
bfs(graph, root)


"""
테스트 케이스 1
4 5 1
1 2
1 3
1 4
2 4
3 4

테스트 케이스 1(정답)
1 2 4 3
1 2 3 4

테스트 케이스 2
5 5 3
5 4
5 2
1 2
3 4
3 1

테스트 케이스 2(정답)
3 1 2 5 4 
3 1 4 2 5
"""
