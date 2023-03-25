# 시간 초과

def prime_num(n):
    

    for i in range(2,n):
        if n%i==0:
            return False
    return True

N, M = map(int, input().split())
for i in range(N,M+1):
    if prime_num(i):
        print(i)


----------------------------------------------------
# 에라토스테네스의 체
def Prime_num(num):
    if num==1:
        return False
    else:
        for n in range(2, int(num**0.5)+1):
            if num % n ==0:
                return False
        return True
M, N = map(int, input().split())

for i in range(M, N+1):
    if Prime_num(i):
        print(i)
