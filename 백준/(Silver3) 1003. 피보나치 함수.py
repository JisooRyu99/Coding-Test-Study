# soultion 실패

def fibonacci(n):
    global zero
    global one

    if n == 0:
        zero+=1
        return 0
    elif n==1:
        one+=1
        return 1
    return fibonacci(n-1), fibonacci(n-2)

T = int(input())
for i in range(T):
    n = int(input())
    zero = 0
    one = 0
    fibonacci(n)
    
    print(zero, one)
    
# 1. 0과 1 이 출력된 갯수를 파악하기 위해 전역변수를 사용
# 2. 함수 안에서 0, 1이 나올때마다 카운팅

=> 시간 초과
-----------------------------------------------------

t = int(input())
 
for x in range(t):
    cnt_0 = [1,0]   # 기본으로 0과 1일 때 개수 초기화시키기
    cnt_1 = [0,1]   # 기본으로 0과 1일 때 개수 초기화시키기
    n = int(input())
    if n>1:     # 0과 1인 경우 이미 리스트에 있으므로 1보다 클 경우 진행
        for i in range(n-1):    
            cnt_0.append(cnt_1[-1])     # 현재 0의 개수는 이전 1의 개수를 가져옴
            cnt_1.append(cnt_0[-2]+cnt_1[-1])       # 현재 1의 개수는 이전 0의 개수+이전 1의 개수
 
    print(cnt_0[n], cnt_1[n])
    
    
    
# 0의 개수 = 이전 1의 개수
# 1의 개수 = 이전 0의 개수 + 이전 1의 개수

