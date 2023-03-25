from itertools import combinations
def solution(numbers):
    answer = []
    num = list(combinations(numbers,2))   # 조합
    
    for i in num:
        answer.append(sum(i))
    
    return sorted(list(set(answer)))    # 중복제거
