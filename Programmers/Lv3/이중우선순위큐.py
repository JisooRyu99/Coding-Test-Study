# https://school.programmers.co.kr/learn/courses/30/lessons/42628

# | 숫자 : 큐에 주어진 숫자를 삽입합니다.
# D 1 : 큐에서 최댓값을 삭제합니다.
# D -1 : 큐에서 최솟값을 삭제합니다.
def solution(operations):
    answer = []
    for oper in operations:
        op, num = oper.split(" ")
        num = int(num)
        if op=='I':
            answer.append(num)
        else:
            if answer:
                if num==1:
                    answer.remove(max(answer))
                else:
                    answer.remove(min(answer))
    if answer: return [max(answer), min(answer)]
    else: return [0,0]