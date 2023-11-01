# https://school.programmers.co.kr/learn/courses/30/lessons/12941

from functools import reduce
def solution(A,B):
    answer=0
    A.sort()
    B.sort(reverse=True)
    
    for i, j in zip(A,B):
        answer+= i*j
    return answer