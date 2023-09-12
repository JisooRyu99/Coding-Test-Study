# https://www.acmicpc.net/problem/6603

from itertools import combinations

while True:
    arr = list(map(int, input().split()))
    K = arr[0]
    S = arr[1:]
    
    if K==0:
        break
   
    for i in (list(combinations(S, 6))):
        print(*i)
    print()