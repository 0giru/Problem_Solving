# 바이러스
from collections import deque

N = int(input())
M = int(input())

queue = deque()

visited = [False] * [N+1]

# 컴퓨터의 수 만큼 빈 리스트를 만들어 그래프를 만들거임
graph = [[] for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)

for i in range(len(graph)):
    graph[i].sort()

def bfs(par_graph,par_start, par_visited):

