from itertools import permutations

def prime_num(num):         # 소수 판별
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:   
            return False
    return True

def solution(numbers):
    answer = 0
    stack=[]
    temp=[]
    for i in range(1,len(numbers)+1):
        temp.extend(permutations(numbers, i)) # numbers을 가지고 순열 만들기
        stack = [int(''.join(i)) for i in temp] 
        # temp 저장된 원소 한 숫자로 만들기
        # ex) ('9','1') -> [91]
    for i in set(stack):
        if prime_num(i):    # 소수 판별
            answer+=1
    return answer