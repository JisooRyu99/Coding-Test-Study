# https://www.acmicpc.net/problem/11725

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

def dfs(graph, v, visited):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = v
            dfs(graph, i, visited)
            
N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N - 1):
    node_a, node_b = map(int, input().split())
    graph[node_a].append(node_b)
    graph[node_b].append(node_a)
    
visited = [False] * (N+1)

dfs(graph, 1, visited)

for x in range(2, N+1):
    print(visited[x])