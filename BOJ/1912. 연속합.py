# https://www.acmicpc.net/problem/1912

N = int(input())
arr = list(map(int, input().split()))

dp = arr

for i in range(1,N):
    dp[i] = max(dp[i], dp[i] + dp[i-1])
print(max(dp))