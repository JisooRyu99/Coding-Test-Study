# https://www.acmicpc.net/problem/15666

n,m = map(int,input().split())
arr = list(map(int,input().split()))

def dfs(start):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(start, len(arr)):
        answer.append(arr[i])
        dfs(i)
        answer.pop()

answer = []
arr = sorted(set(arr))
dfs(0)