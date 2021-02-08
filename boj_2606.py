# 바이러스
from collections import deque

N = int(input())
M = int(input())

queue = deque()
result = []

visited = [False] * (N+1)

graph = [[] for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for i in range(len(graph)):
    graph[i].sort()

def bfs(par_graph,par_start, par_visited):
    queue.append(par_start)
    visited[par_start] = True
    while queue:
        temp = queue.popleft()
        result.append(temp)
        for i in par_graph[temp]:
            if not par_visited[i]:
                queue.append(i)
                par_visited[i] = True

bfs(graph, 1, visited)

print(len(result)-1)