# https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):
    answer = []
    l,r = 0, -1
    s_sum = 0
    
    while True:
        if s_sum < k:
            r+=1
            if r >= len(sequence):
                break
            s_sum += sequence[r]
        else:
            s_sum -= sequence[l]
            if l >= len(sequence):
                break
            l+=1
        if s_sum==k:
            answer.append([l,r])
    answer.sort(key=lambda x:(x[1]-x[0], x[0]))
    return answer[0]