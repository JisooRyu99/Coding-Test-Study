import sys
import heapq 
sys.setrecursionlimit(10**9)        
input = sys.stdin.readline

T = int(input())
heap = []
for i in range(T):
    num = int(input())
    if num == 0 and heap:
        print(heapq.heappop(heap))
    elif num==0 and not heap:
        print(0)
    else:
        heapq.heappush(heap, num)