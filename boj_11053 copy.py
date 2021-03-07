# 가장 긴 증가하는 부분수열 https://www.acmicpc.net/problem/11053

N = int(input())

array = list(map(int, input().split()))
dp = [1 for i in range(N)]
temp_list = list()
result = list()

for i in range(N):
    for j in range(i):
        if array[i] > array[j] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1

temp = max(dp)

for i in range(len(dp)-1, -1, -1):
    if dp[i] == temp:
        result.append(array[i])
        temp -= 1
        if temp == -1:
            break

result.reverse()

print(max(dp))
for i in result:
    print(i, end=' ')