def solution(want, number, discount):
    answer = 0
    want_list = []
    for i in range(len(want)):
        want_list+=[want[i]]*number[i]

    for i in range(len(discount)-sum(number)+1):
        if sorted(discount[i:i+10]) == sorted(want_list):
            answer+=1
    return answer