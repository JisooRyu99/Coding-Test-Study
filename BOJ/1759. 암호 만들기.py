# https://www.acmicpc.net/problem/1759

from itertools import combinations

l, c = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort()
for i in (list(combinations(arr,l))):
    cnt = 0
    for j in i:
        if j in 'aeiou':
           cnt+=1
    
    if cnt>=1 and cnt<=(l-2):
        print(''.join(i)) 