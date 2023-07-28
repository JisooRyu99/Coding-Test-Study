from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append([numbers[0]*-1, 0])
    queue.append([numbers[0], 0])
    
    while queue:
        num, idx = queue.popleft()
        idx+=1

        if idx < len(numbers):
            queue.append([numbers[idx]+num, idx])
            queue.append([numbers[idx]*-1 + num, idx])
            
        else:
            if num == target:
                answer+=1
    return answer