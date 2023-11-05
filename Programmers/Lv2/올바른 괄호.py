# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = []
    s = list(s)
    if len(s)<2 and s[0] == ')':
        return False
    for i in s:
        if i=='(':
            answer.append(i)
        else:
            if not answer:
                return False
            else:
                answer.pop()
    if not answer:
        return True
    else:
        return False