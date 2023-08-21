# https://school.programmers.co.kr/learn/courses/30/lessons/138476

import collections
def solution(k, tangerine):
    answer = 0
    tangerine_cnt = collections.Counter(tangerine)
    
    for x in sorted(tangerine_cnt.values(), reverse=True):
        if k<=0:
            break
        k-=x
        answer+=1
        
    return answer