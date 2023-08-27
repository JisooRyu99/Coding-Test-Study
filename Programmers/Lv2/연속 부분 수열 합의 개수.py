def solution(elements):
    answer = set()
    elements_len = len(elements)
    elements *=2
    idx = 0
    
    while idx < elements_len:
        for i in range(elements_len):
            answer.add(sum(elements[i:idx+i+1]))
        idx+=1
    
    return len(answer)