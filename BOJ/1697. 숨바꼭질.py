from collections import deque

def solution():
    while queue:
        x, idx = queue.popleft()
        
        if x == K:
            return idx
        
        idx+=1
        if 0 < x < K and x*2 < MAX and not visited[2*x]:
            visited[2*x] = 1
            queue.append([2*x, idx])
        
        if x < K and x+1 < MAX and not visited[x+1]:
            visited[x+1] = 1
            queue.append([x+1, idx])
        
        if 0 <= x-1 and not visited[x-1]:
            visited[x-1] = 1
            queue.append([x-1, idx])

N, K = map(int, input().split())         
MAX = 100001
visited = [0]*(MAX+1)
queue = deque()
queue.append([N,0])
print(solution())