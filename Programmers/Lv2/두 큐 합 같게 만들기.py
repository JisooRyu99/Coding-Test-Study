from collections import deque
def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    if (sum1+ sum2) % 2 != 0:
        return -1
    while True:
        if answer == len(queue1) *3 :
            return -1
        
        if sum1 > sum2:
            tmp = queue1.popleft()
            queue2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
            
        elif sum1 < sum2:
            tmp = queue2.popleft()
            queue1.append(tmp)
            sum1 += tmp
            sum2 -= tmp
        else:
            return answer
        answer+=1
