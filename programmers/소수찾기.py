from itertools import permutations

def prime_num(num):
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
        temp.extend(permutations(numbers, i))
        stack = [int(''.join(i)) for i in temp]
    for i in set(stack):
        if prime_num(i):
            print(i)
            
            answer+=1
    return answer