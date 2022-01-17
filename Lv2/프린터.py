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
