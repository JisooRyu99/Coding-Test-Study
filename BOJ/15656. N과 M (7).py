# https://www.acmicpc.net/problem/15656

def dfs():
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(n):
        visited[i] = True
        answer.append(arr[i])
        dfs()
        answer.pop()
        visited[i] = False

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answer = []
visited = [False] * (n)
dfs() 