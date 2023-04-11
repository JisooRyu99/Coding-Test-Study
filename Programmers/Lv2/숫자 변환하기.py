[숫자 변환하기](https://school.programmers.co.kr/learn/courses/30/lessons/154538#qna)

# 시간초과
from collections import deque
def solution(x, y, n):
    answer = 0
    if x==y: return 0
    queue = deque([[x,0]])
    
    while queue:
        x, cnt = queue.popleft()
        cnt+=1
        if x+n<y:
            queue.append([x+n, cnt])
        elif x+n==y:
            return cnt
        
        if x*2<y:
            queue.append([x*2, cnt])
        elif x*2==y:
            return cnt
    
        if x*3<y:
            queue.append([x*3, cnt])
        elif x*3==y:
            return cnt
        
    return -1
          
#################################################
from collections import deque, defaultdict
def solution(x, y, n):
    answer = 0
    if x==y: return 0
    queue = deque([[x,0]])
    duplication = defaultdict(int)
    
    while queue:
        x, cnt = queue.popleft()
        cnt+=1
        
        if duplication[x] ==1:
            continue
        else:
            duplication[x] = 1
        
        if x+n<y:
            queue.append([x+n, cnt])
        elif x+n==y:
            return cnt
        
        if x*2<y:
            queue.append([x*2, cnt])
        elif x*2==y:
            return cnt
    
        if x*3<y:
            queue.append([x*3, cnt])
        elif x*3==y:
            return cnt
        
    return -1
          
 # defulatdict를 이용해서 어떤 숫자는 이미 끝냈는지 확인
