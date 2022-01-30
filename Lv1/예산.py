# 시간 초과

from itertools import combinations

def solution(d, budget):
    answer = []
    
    result = [seq for i in range(len(d), 0, -1) for seq in combinations(d, i) if sum(seq) <= budget]
    
    for i in result:
        answer.append(len(i))
    return max(answer)
---------------------------------------------------------------------------------------------------------------
