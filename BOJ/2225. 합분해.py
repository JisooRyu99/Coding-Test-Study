#https://www.acmicpc.net/problem/2225

N, K = map(int, input().split())

MAX = 209
dp = [[0] * MAX for _ in range(MAX)]

for k in range(MAX):
    dp[1][k] = 1
    dp[2][k] = k+1

for i in range(2,MAX):
    dp[i][1] = i
    for j in range(2,MAX):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000000
print(dp[K][N])