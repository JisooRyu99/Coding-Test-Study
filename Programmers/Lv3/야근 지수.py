# https://school.programmers.co.kr/learn/courses/30/lessons/12927

import heapq
def solution(n, works):
    heap = [-w for w in works]
    heapq.heapify(heap)
    
    while n>0:
        max_value = heapq.heappop(heap)
        heapq.heappush(heap, max_value+1)
        n-=1
    
    return sum([i**2 for i in heap if i<0])

#################### 시간 초과 ####################

'''
def solution(n, works):
    answer = 0
    
    while n > 0:
        works.sort(reverse=True)
        for w in range(len(works)):
            if works[w] >0:
                works[w] -=1
            n-=1
            break
            
        
    return sum([i**2 for i in works])
'''