# https://www.acmicpc.net/problem/1182

n, m = map(int,input().split())
arr= list(map(int,input().split()))
answer=0
from itertools import combinations
for i in range(1,len(arr)+1):
    for j in (list(combinations(arr,i))):
        if (sum(j))==m:
            answer+=1
print(answer)
