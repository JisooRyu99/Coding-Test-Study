# https://school.programmers.co.kr/learn/courses/30/lessons/154539

def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)
    
    for n in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[n]:
            answer[stack.pop()] = numbers[n]
        stack.append(n)

    return answer