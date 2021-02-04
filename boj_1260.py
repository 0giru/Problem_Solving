n, m, v = map(int, input().split())

# empty_set = set()
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = []

for _ in range(m):
    temp_list = list(map(int, input().split()))
    temp_num1 = temp_list[0]
    temp_num2 = temp_list[1]
    graph[temp_num1].append(temp_num2)
    graph[temp_num1].sort()
    graph[temp_num2].append(temp_num1)
    graph[temp_num2].sort()

# print(graph)

def dfs(par_graph, par_v, par_visited):
    visited[par_v] = True
    result.append(par_v)
    for i in par_graph[par_v]:
        if not visited[i]:
            dfs(par_graph, i, par_visited)

dfs(graph, v, visited)

print(result)

