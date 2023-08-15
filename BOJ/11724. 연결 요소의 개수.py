# https://www.acmicpc.net/problem/11724

import sys
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
    return

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    tmp = list(map(int, input().split()))
    graph[tmp[0]].append(tmp[1])
    graph[tmp[1]].append(tmp[0])

visited = [False] * (N+1)
cnt=0
for i in range(1, N+1):
    if not visited[i]:
        dfs(graph, i, visited)
        cnt+=1
print(cnt)