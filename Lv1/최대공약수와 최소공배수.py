import math


def lcm(x,y):   # 최소공배수
    return x*y//math.gcd(x,y)
def solution(n, m):
    return math.gcd(n,m), lcm(n,m)  # math.gcd : 최대공약수
