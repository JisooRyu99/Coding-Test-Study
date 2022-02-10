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

def solution(number):
    numbers = [True] * (number + 1) 
    answer = 0

    for num in range(2,int(math.sqrt(number))+1):   # 2부터 시작해서 특정 수의 배수에 해당하는 수를 모두 지운다 (이때 자기 자신은 지우지 않고, 이미 지운 수는 건너 뜀)
        if numbers[num] == False:
            continue;

        for i in range(num+num,number+1,num):
            numbers[i] = False

    for i in range(2,number+1):
        if numbers[i] == True:
            answer+=1

    return answer
