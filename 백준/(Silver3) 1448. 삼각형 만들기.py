'''
a+b > c
a> c-b, b> c-a
'''
'''
from itertools import combinations

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

result = []
combi = (list(combinations(lst,3)))
for i in range(len(combi)):
    if combi[i][2] < combi[i][0] + combi[i][1]:
        print(combi[i])
        result.append(sum(combi[i]))

if not result:
    print(-1)
else:
    print(max(result))'''
-----------------------------------------------------------------
# from itertools import combinations 을 사용하면 시간초과 발생
-----------------------------------------------------------------
import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

lst.sort()
result = 0
for i in range(len(lst)-2):
    if lst[i+2] < lst[i]+lst[i+1]:
        result = (lst[i]+lst[i+1]+lst[i+2])

if not result:
    print(-1)
else:
    print(result)
