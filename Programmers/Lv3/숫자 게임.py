# https://school.programmers.co.kr/learn/courses/30/lessons/12987

def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    for a in A:
        if a< B[0]:
            answer+=1
            B.pop(0)
        
    return answer