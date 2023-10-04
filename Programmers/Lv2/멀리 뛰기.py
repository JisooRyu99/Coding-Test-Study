# https://school.programmers.co.kr/learn/courses/30/lessons/12914#

def solution(n):
    dp = [0] * (10002)
    dp[1] = 1
    dp[2] = 2
    
    if n > 2:
        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    
    return dp[n] % 1234567