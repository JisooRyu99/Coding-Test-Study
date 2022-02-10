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

n = 1000	# 2부터 1000까지 모든 수에 대하여 소수를 찾을 것이다.
array = [True for i in range(n + 1) # 0,1을 제외한 모든 숫자가 소수(True)인 것으로 설정하고 시작한다.

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인
	if array[i] == True:	# i가 소수인 경우
    	# i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
        	array[i * j] = False
            j += 1
            
#모든 소수 출력
for i range(2, n + 1):
	if array[i]:
    	print(i, end = ' ')
