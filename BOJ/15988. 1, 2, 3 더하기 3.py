import sys
sys.setrecursionlimit(10**9)    
input = sys.stdin.readline
T = int(input())
MAX = 1000001
dp = [0] * MAX
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4,MAX):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])%1000000009
for i in range(T):
    N = int(input())
    print(dp[N])