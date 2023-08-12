from collections import deque
# import sys

# sys.setrecursionlimit(10**9)        
# input = sys.stdin.readline
N, M = map(int, input().split())

maps = []

for _ in range(N):
  maps.append(list(map(int, input())))

def dfs(maps):
    queue = deque()
    queue.append([0,0])
    
    graph = [[-1 for _ in range(M)] for _ in range(N)]
    graph[0][0] = 1
    
    dy = [0,0,-1,1]
    dx = [-1,1,0,0]
    
    while queue:
        y, x= queue.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            
            if 0 <= ny < N and 0 <= nx < M and maps[y][x] == 1:
                if graph[ny][nx] == -1:
                    graph[ny][nx] = graph[y][x]+ 1
                    queue.append([ny,nx])

    return graph[-1][-1]

print(dfs(maps))