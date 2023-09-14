# https://school.programmers.co.kr/learn/courses/30/lessons/76502

def check(s):
    stack = []
    s_dict = {"[":"]","{":"}","(":")"}
    
    for i in s:
        if not stack: stack.append(i)
        elif stack[-1] in s_dict:
            if s_dict[stack[-1]]==i:
                stack.pop()
            else: stack.append(i)
        else: stack.append(i)

    return stack
def solution(s):
    answer = 0
    
    for i in range(len(s)):
        new_s = s[i:]+s[:i]
        if not check(new_s): answer+=1
    return answer