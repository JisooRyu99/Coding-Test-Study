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
