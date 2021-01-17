import sys
from collections import deque

num_nodes, num_loops, root = list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(num_nodes + 1)]

for _ in range(num_loops):
    node1, node2 = list(map(int, sys.stdin.readline().split()))
    graph[node1].append(node2)
    graph[node2].append(node1)
for n in range(num_nodes + 1): graph[n].sort()


def dfs(graph, root_node):
    visit, stack = [], [root_node]

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(reversed(graph[node]))

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
