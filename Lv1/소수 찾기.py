# 시간 초과..

def prime_number(num):
    for n in range(2,num):
        if num%n==0:
            return False
    return True

def solution(n):
    answer = []  
    for i in range(2,n+1):
        if prime_number(i)==True:
            answer.append(i)
    return len(answer)
    
    
-----------------------------------------------------------------------------------------

# < 아라토스테네스의 체 >
# 소수를 판별하는 알고리즘
# 소수들을 대량으로 빠르고 정확하게 구하는 방법

import math

def Prime_num(num):
    if num==1:
        return False
    else:
        for n in range(2, int(num**0.5)+1):	# n의 제곱근까지만 
            if num % n ==0:
                return False
        return True
M, N = map(int, input().split())

for i in range(M, N+1):
    if Prime_num(i):
        print(i)
