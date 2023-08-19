# https://www.acmicpc.net/problem/2075

import heapq 

N = int(input())
heap = []

for i in range(N):
    num = list(map(int, input().split()))
    if not heap:
        for n in num:
            heapq.heappush(heap, n)
    else:
        for n in num:
            if heap[0] < n:
                heapq.heappush(heap, n)
                heapq.heappop(heap)
print(heap)
        