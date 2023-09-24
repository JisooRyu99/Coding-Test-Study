# https://school.programmers.co.kr/learn/courses/30/lessons/17686

import re
def solution(files):
    arr = []
    answer = []
    for f in files:
        arr.append(re.split(r'(\d+)', f))      
    arr.sort(key = lambda x : (x[0].lower(), int(x[1])))
    for i in arr:
        answer.append("".join(i))
    return answer