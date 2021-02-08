from collections import deque

# dfs 함수
def dfs(par_graph, par_v, par_visited):
    visited[par_v] = True
    result_dfs.append(par_v)
    for i in par_graph[par_v]:
        if not visited[i]:
            dfs(par_graph, i, par_visited)

#bfs 함수
def bfs(par_graph, par_v, par_visited):
    visited[par_v] = True
    queue.append(par_v)
    while queue:
        v = queue.popleft()
        result_bfs.append(v)
        for i in par_graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

queue = deque()

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result_dfs = []
result_bfs = []

for _ in range(m):
    temp_list = list(map(int, input().split()))
    temp_num1 = temp_list[0]
    temp_num2 = temp_list[1]
    graph[temp_num1].append(temp_num2)
    graph[temp_num1].sort()
    graph[temp_num2].append(temp_num1)
    graph[temp_num2].sort()

dfs(graph, v, visited)
visited = [False] * (n+1)
bfs(graph, v, visited)

for i in result_dfs:
    if i == result_dfs[len(result_dfs)-1]:
        print(i, end='\n')
    else:
        print(i, end=' ')
for i in result_bfs:
    print(i, end=' ')