import sys
import heapq 

sys.setrecursionlimit(10**9)        
input = sys.stdin.readline

T = int(input())
heap = []

for i in range(T):
    num = int(input())
    if num == 0:
        if heap: print(heapq.heappop(heap)[1])
        else: print(0)
    else:
        '''
        heappush() 함수에 두 번째 인자에 튜플을 사용할 경우
        튜플의 첫 번째 항목을 기준으로 우선순위를 가지게 된다.
        '''
        heapq.heappush(heap, (abs(num), num))   