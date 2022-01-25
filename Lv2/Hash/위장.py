import collections
def solution(clothes):
    answer=1
    count = collections.Counter([c for _, c in clothes])        
    # 각 category 별로 count 
    
    for v in count.values():
        answer*=(v+1)
        
        
    return answer-1         # 모두 안 입는 경우


# 의상의 종류 A에서 1개를 선택하거나 선택 안하거나 (B,C 동일)
# => (A의 개수+1) * (B의 개수+1) * (C의 개수+1) -1 (아무것도 입지 않는 경우) 을 하면 조합을 구할 수 있음.
