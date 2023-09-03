# https://school.programmers.co.kr/learn/courses/30/lessons/67259

from collections import deque
import sys
def solution(board):
    answer = 0
    dy = [0,0,-1,1]
    dx = [-1,1,0,0]
    
    N = len(board)
    graph = [[[sys.maxsize]*4 for _ in range(N)] for _ in range(N)]
    queue = deque()
    
    queue.append([0,0,-1]) # y,x,dir
    graph[0][0] = [0,0,0,0]
    
    while queue:
        y,x,direction = queue.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            cost = 100
            if i!=direction and direction!=-1:
                cost +=500
            if 0<=ny<N and 0<=nx<N and board[ny][nx]!=1:
                if graph[ny][nx][i] > graph[y][x][direction] + cost:
                    graph[ny][nx][i] = graph[y][x][direction] + cost
                    queue.append([ny,nx,i])
    
    return min(graph[-1][-1])