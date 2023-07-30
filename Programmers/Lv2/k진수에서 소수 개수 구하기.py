def convert(n,base):
    T = '0123456789ABCDEF'
    q,r = divmod(n,base)
    return convert(q,base) + T[r] if q else T[r]
import math
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
from itertools import combinations
def solution(n, k):
    answer = 0
    new_num = convert(n,k)
    for i in (new_num.split('0')):
        if (i):
            if is_prime(int(i)):
                answer+=1
                
    return answer