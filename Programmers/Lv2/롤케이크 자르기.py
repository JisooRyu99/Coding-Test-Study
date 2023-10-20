# https://school.programmers.co.kr/learn/courses/30/lessons/132265

from collections import Counter

def solution(topping):
    dic = Counter(topping)
    roll_cake = set()
    answer = 0
    for t in topping:
        dic[t]-=1
        roll_cake.add(t)
        if dic[t] == 0:
            dic.pop(t)
        if len(dic) == len(roll_cake):
            answer+=1
        
    return answer

#################### 시간 초과 ####################
'''
def solution(topping):
    answer = 0
    idx = len(topping)-1
    l,r = [], []
    while idx>0:
        
        l = topping[:idx+1]
        r = topping[idx+1:]
        idx-=1
        if len(set(l)) == len(set(r)):
            answer+=1
        
    return answer
'''