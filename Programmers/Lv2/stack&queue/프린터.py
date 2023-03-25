def solution(priorities,location):
    ans = 0

    while True:
        m = max(priorities)
        v = priorities.pop(0)     
        if m==v:      # priorities의 첫번째가 가장 큰 원소이면
            ans+=1    # answer+=1 
            if location==0:     # location==0 이면 while 문 빠져나오기 
                break
            else:
                location-=1     # location-=1
            m = max(priorities)   # max 값 갱신
        else:
            priorities.append(v)   # priorities 맨뒤로 보내기
            if location==0:       
                location= len(priorities)-1
            else:
                location-=1
    return ans

solution([1, 1, 9, 1, 1, 1], 0)


-----------------------------------------------------------------------------
# deque 

def solution(priorities, location):
    answer = 0
    from collections import deque

    deq = deque([(v,i) for i,v in enumerate(priorities)])

    while len(deq):
        item = deq.popleft()
        if deq and max(deq)[0] > item[0]:
            deq.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer


------------------------------------------------------------------------------------
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):       
            # any : 전달받은 자료형의 element 중 하나라도 True일 경우 True를 돌려준다 (만약 empty 값을 argument로 넘겨주었다면 False를 돌려줌
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
