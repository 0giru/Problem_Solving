# 1의 개수를 세는 BFS 표준 코드

import sys
from collections import deque
sys.setrecursionlimit(10000)


N, M = map(int, input().split())

graph = []
count = 0
result = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 리스트 컴프리헨션 정리
for i in range(N):
    graph.append(list(map(int, input())))

def dfs(par_x, par_y):
    global count

    if graph[par_x][par_y] == 1:
        graph[par_x][par_y] = 0
        count += 1
    elif graph[par_x][par_y] == 0:
        return
    
    for i in range(4):
        new_x = par_x + dx[i]
        new_y = par_y + dy[i]

        if new_x < 0 or new_x >= N or new_y < 0 or new_y >= M:
            continue

        dfs(new_x, new_y)

    graph[par_x][par_y] = 1


dfs(0, 0)
print(count)