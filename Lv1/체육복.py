
# lost_ = [(i) for i in lost for j in reserve if (i-j)==1 ]
# 다시 시도해보기


def solution(n,lost, reserve):

    only = n-len(set(reserve)|set(lost))  # 자기것
    only_reserve = list(set(reserve)-set(lost)) # 여벌이 있는 학생 (도난 당한 학생과 같은 사이즈 제외)
    only_lost = list(set(lost)-set(reserve)) # 여벌이 있는 학생과 같은 사이즈가 없는 도난 당한 학생
    only_reserve.sort()
    only_lost.sort()
    
    for i in only_reserve:      # 앞 뒤로 학생들 
        left = i-1
        right = i+1
        if left in only_lost:
            only_lost.remove(left)
        elif right in only_lost:
            only_lost.remove(right)
            
    return n-len(only_lost)
