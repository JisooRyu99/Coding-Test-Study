# https://school.programmers.co.kr/learn/courses/30/lessons/12902

def solution(n):
    dp = [3,11]
    if n%2!=0: return 0
    if n<=4 : return dp[n//2-1]
    for x in range(2, n//2):
        dp.append(((dp[x-1] * 4) - dp[x-2])%1000000007)

    return dp[-1]

'''
n = 1 : 0
n = 2 : 3
n = 3 : 0
n = 4 : 11
n = 6 : 41

f(x) = f(x-2) * 4 - f(x-4)
'''