# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque
def solution(maps):
    answer = 0
    r,c = len(maps), len(maps[0])
    queue=deque()
    queue.append([0,0])
    graph = [[-1 for _ in range(len(maps[0]))]for _ in range(len(maps))]
    graph[0][0] = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            ny = dy[i]+y
            nx = dx[i]+x
            if 0<=ny<r and 0<=nx<c and maps[y][x]==1:
                if graph[ny][nx]==-1:
                    graph[ny][nx] = graph[y][x]+1
                    queue.append([ny,nx])
    return graph[-1][-1]