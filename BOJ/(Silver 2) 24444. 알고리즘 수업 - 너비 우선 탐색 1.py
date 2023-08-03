from collections import deque
import sys
input = sys.stdin.readline  # input()으로 받을 시 시간초과

cnt = 1
def bfs(graph, v, visited):
    global cnt
    queue = deque([v])
    visited[v] = cnt
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                cnt+=1
                visited[i] = cnt
                
                
N, M, v = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    tmp = list(map(int, input().split()))
    graph[tmp[0]].append(tmp[1])
    graph[tmp[1]].append(tmp[0])

for i in range(N+1):
    graph[i].sort()

visited = [0] * (N+1)

bfs(graph, v, visited)

for i in range(1, N+1):
    print(visited[i])