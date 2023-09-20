# https://school.programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    answer = '124'
    if n<4:
        return answer[n-1]
    else:
        div,mod = divmod(n-1,3)
        return solution(div) + answer[mod]