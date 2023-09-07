# https://www.acmicpc.net/problem/15663

n,m = map(int,input().split())
arr = list(map(int,input().split()))

from itertools import permutations

data = (set(list(permutations(arr,m))))
for i in sorted(data):
    print(*i)