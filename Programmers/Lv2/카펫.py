# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    total = brown+yellow
    for b in range(1,total):
        if total%b==0:
            a = total//b
            if a*b==total and (a-2)*(b-2)==yellow:
                return(a,b)
                
    return answer