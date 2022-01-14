# 입출력 순서에 대한 업급 -> stack, queue 
# --> pop으로 해결하기

# stack은 pop()으로
# queue는 pop(0)

def solution(progresses, speeds):
    n=0
    cnt=0
    answer=[]
    while len(progresses)>0:
        if progresses[0] + n*speeds[0] >99:
            progresses.pop(0)
            speeds.pop(0)
            cnt+=1
        else:
            print(cnt)
            if cnt>0:
                answer.append(cnt)
                cnt=0
            n+=1
    answer.append(cnt)
    return answer

# 1. 100이 될때까지 loop 설정
# 1-1. loop돌 때 동안 n+=1
# 2. 첫번째 원소가 100이 되면 progress, speeds에서 pop하고 cnt+=1
# 3. 그 다음 원소도 계속 loop 
# 3-1. 이때, cnt>0 이라면 answer에 저장하고 cnt 초기화
# 3-2. n+=1
# 4. 마지막 원소가 100 넘어서 loop 빠져나오면 answer에 cnt 저장
