# https://www.acmicpc.net/problem/15664

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

from itertools import combinations

data = (set(list(combinations(arr,m))))

for i in sorted(data):
    print(*i)