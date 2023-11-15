# https://www.acmicpc.net/problem/14002

n = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(n+1)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
MAX = max(dp)
print(MAX)

answer = []
for i in range(n-1,-1,-1):
    if dp[i] == MAX:
        answer.append(arr[i])
        MAX-=1
answer.sort()
print(*answer)