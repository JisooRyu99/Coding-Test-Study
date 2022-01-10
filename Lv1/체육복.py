def solution(n, lost, reserve):
    only = n-len(set(reserve)|set(lost))
    # 자기 체육복만 있는 학생
    reserve_ = set(reserve)-set(lost)
    # 여벌이 있는 학생 (도난 당한 학생과 같은 사이즈 제외)
    lost_ = list(set(lost) - set(reserve))
    # 여벌이 있는 학생과 같은 사이즈가 없는 도난 당한 학생
    reserve.sort()
    lost.sort()

    for i in reserve_:
        front = i - 1 
        back = i + 1 
        if front in lost_:  
            # 앞 학생이 여벌이 있으면 lost_에서 제거
            lost_.remove(front)
        elif back in lost_:
            lost_.remove(back)
            # 뒷 학생이 여벌이 있으면 lost_에서 제거
    return n-len(lost_)

# lost_ = [(i) for i in lost for j in reserve if (i-j)==1 ]
# 다시 시도해보기
