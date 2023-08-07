import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
def dfs(y, x):
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        
        if 0<=ny<N and 0<=nx < M:
            if maps[ny][nx] == 1:
                maps[ny][nx] = -1
                dfs(ny, nx)
T = int(input())
counts = []

for _ in range(T):
    M, N, K = map(int, input().split())
    maps = [[0] * (M) for _ in range(N)]
    cnt = 0
    
    for _ in range(K):
        x, y = map(int, input().split())
        maps[y][x] = 1
        
    for y in range(N):
        for x in range(M):
            if maps[y][x] == 1:
                dfs(y, x)
                cnt += 1
    counts.append(cnt)

for i in counts:
    print(i)