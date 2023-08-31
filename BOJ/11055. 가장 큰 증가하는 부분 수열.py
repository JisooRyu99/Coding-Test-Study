# https://www.acmicpc.net/problem/11055

N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N
dp[0] = arr[0]

for i in range(1,N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], arr[i] + dp[j])
        else:
            dp[i] = max(dp[i], arr[i])

print(max(dp))