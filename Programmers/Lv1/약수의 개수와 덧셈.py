def solution(left, right):
    answer = 0
    
    for i in range(left,right+1):
        cnt=0
        for num in range(1,i+1):
            if i%num==0:    
                cnt+=1      # 약수 개수 count
        if cnt%2==0:        # 약수 개수가 짝수이면 +
            answer+=i
        else: answer = answer-i # 약수 개수가 홀수이면 -
    return answer
