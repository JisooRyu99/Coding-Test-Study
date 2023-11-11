# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 1
    clothes_dict = {}
    
    for name, types in clothes:
        if types in clothes_dict:
            clothes_dict[types].append(name)
        else:
            clothes_dict[types] = [name]
        
    for k,v in clothes_dict.items():
        answer = answer * (len(clothes_dict[k]) + 1)
    return answer - 1