# https://www.acmicpc.net/problem/15665

n,m = map(int,input().split())
arr = list(map(int,input().split()))

def dfs():
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    for i in arr:
        answer.append(i)
        dfs()
        answer.pop()

answer = []
arr = sorted(set(arr))
dfs()