from collections import Counter
def solution(input_string):
    answer = set()
    count = Counter(input_string)
    stack = []
    
    for x in input_string:
        if not stack: stack.append(x)
        else:
            if stack[-1] == x:
                stack.append(x)
            else:
                if count[stack[-1]]!=len(stack):
                    answer.add(stack[-1])
                stack = [x]
                
    return "".join(sorted(answer)) if answer else 'N'

# 문제 : https://school.programmers.co.kr/learn/courses/15008/lessons/121683?language=python3
