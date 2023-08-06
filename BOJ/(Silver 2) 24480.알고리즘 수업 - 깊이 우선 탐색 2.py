import sys

cnt = 1

def dfs(graph, v, visited):
    global cnt
    visited[v] = cnt
    
    for i in graph[v]:
        if visited[i] == 0:
            cnt+=1
            dfs(graph, i, visited)

sys.setrecursionlimit(10**9)
input = sys.stdin.readline
        
N, M, v = map(int, input().split())

graph = [[] for _ in range(N+1)]
for i in range(M):
    tmp = list(map(int, input().split()))
    graph[tmp[0]].append(tmp[1])
    graph[tmp[1]].append(tmp[0])
    
for i in range(N+1):
    graph[i].sort(reverse=True)
    
visited = [0] * (N+1)
dfs(graph, v, visited)

for i in range(1,N+1):
    print(visited[i])
