# https://www.acmicpc.net/problem/15655

def dfs(start):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(start, n):
        if not visited[i]:
            visited[i] = True
            answer.append(arr[i])
            dfs(i+1)
            answer.pop()
            visited[i] = False

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answer = []
visited = [False] * (n)
dfs(0)
            