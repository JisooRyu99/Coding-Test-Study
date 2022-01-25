import collections
def solution(clothes):
    answer=1
    count = collections.Counter([c for _, c in clothes])        
    # 각 category 별로 count 
    
    for v in count.values():
        answer*=(v+1)
        
        
    return answer-1         # 모두 안 입는 경우
