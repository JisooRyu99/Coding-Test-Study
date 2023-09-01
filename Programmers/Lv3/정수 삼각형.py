# https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    answer = 0
    N = len(triangle)
    dp = [triangle[i] + [-1] * (N-len(triangle[i])) for i in range(N)]

    for i in range(1,N):
        for j in range(N):
            dp[i][j] = max(dp[i-1][j] + dp[i][j], dp[i-1][j-1] + dp[i][j])
    return max(dp[-1])