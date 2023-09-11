# https://www.acmicpc.net/problem/10974

from itertools import permutations
n = int(input())
lst = [i for i in range(1,n+1)]
for n in (list(permutations(lst))):
    print(*n)