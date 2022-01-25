def solution(N, stages):
    answer = []
    length = len(stages)
    for i in range(1, N+1):
        count = stages.count(i)
        # 실패율 = 도달하지못한인원/스테이지에 도달한 수
        # 스테이지에 도달한 유저가 없는 경우 
        if count == 0:
            fail = 0
        else:
            fail = count / length
        answer.append((i, fail))
        # length에서 도달하지 못한 인원은 뺀다
        length -= count
    
    # 실패율 기준으로 내림차순
    answer = sorted(answer, key=lambda t: t[1], reverse=True)
    answer = [i[0] for i in answer]
    return answer


'''
도달+클리어x / 스테이지 도달
N : 전체 스테이지 개수
stage : 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열
retrun : 실패율이 높은 스테이지부터 내림차순

{"1":1,"2":3,"3":2,"4":1,"6":1}

'''
