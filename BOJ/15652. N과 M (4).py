# https://www.acmicpc.net/problem/15652

n,m= map(int,input().split())

answer = []

def dfs(s):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    
    for i in range(s, n+1):
        answer.append(i)
        dfs(i)
        answer.pop()
dfs(1)