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

