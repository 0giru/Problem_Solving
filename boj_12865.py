평범한 배낭 https://www.acmicpc.net/problem/12865

N, K = map(int, input().split())

weight = [0]
value = [0]
result = 0
cur = 0

graph = [[0]*(K+1) for _ in range(N+1)]

for _ in range(N):
    W, V = map(int, input().split())
    weight.append(W)
    value.append(V)

for i in range(1, N+1):
    for w in range(K+1):
        if weight[i] <= w:
            graph[i][w] = max(graph[i-1][w], graph[i-1][w-weight[i]]+value[i])
        else:
            graph[i][w] = graph[i-1][w]

print(graph[N][K])

재귀 이용한 백트래킹 - 시간초과
# 평범한 배낭 https://www.acmicpc.net/problem/12865

N, K = map(int, input().split())

weight = []
value = []
result = 0

for _ in range(N):
    W, V = map(int, input().split())
    weight.append(W)
    value.append(V)

def Recursion(idx, lim, val):
    global result
    
    # 현재 배낭의 무게보다 많이 나가면 재귀 종료
    if lim > K:
        return
    if idx == N:
        if val > result:
            result = val
        return

    # i번째 물건을 선택함
    Recursion(idx+1, lim+weight[idx], val+value[idx])
    # i번째 물건을 선택하지 않음
    Recursion(idx+1, lim, val)

Recursion(0, 0, 0)
print(result)