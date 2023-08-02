from math import gcd
from functools import reduce

def solution(arr):
    for i in range(len(arr)-1):
        print(arr[i]//gcd(arr[i],arr[i+1]))
    return reduce(lambda x,y : x*y//gcd(x,y), arr)