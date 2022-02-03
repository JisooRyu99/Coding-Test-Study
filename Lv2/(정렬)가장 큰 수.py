# 시간 초과

from itertools import permutations
def solution(numbers):
    answer = []
    number_list = list(permutations(numbers,len(numbers)))
    
    for n in number_list:
        answer.append("".join(map(str,n)))
    
    return max(answer)
--------------------------------------------------------------------------

