# https://www.acmicpc.net/problem/1260

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
n,m,v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    tmp = list(map(int, input().split()))
    graph[tmp[0]].append(tmp[1])
    graph[tmp[1]].append(tmp[0])
for i in range(n+1):
    graph[i].sort()

visited = [False] * (n+1)
dfs(graph,v, visited)
print()
visited = [False] * (n+1)
bfs(graph, v, visited)