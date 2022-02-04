# 시간 초과

from itertools import combinations
def solution(number, k):
    answer = []
    
    result = list(map(str,number))
    lst = (list(combinations(result,len(result)-k)))
    for i in lst:
        answer.append("".join(map(str,i)))
    
    return max(answer)

--------------------------------------------------------------------------------------------
