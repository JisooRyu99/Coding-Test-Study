# https://www.acmicpc.net/problem/2309

from itertools import combinations

N = 9
arr = [int(input()) for _ in range(N)]
arr.sort()
for i in list(combinations(arr, 7)):
    if sum(i)==100:
        result = i
for i in result:
    print(i)