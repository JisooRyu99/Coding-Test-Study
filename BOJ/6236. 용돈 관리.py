import sys
input = sys.stdin.readline

N, M = map(int, input().split())
money = [int(input()) for _ in range(N)]

start, end = min(money), sum(money)

while start <= end:
    mid = (start+end) // 2
    K = mid
    cnt=1
    
    for i in money:
        if K < i:
            K = mid
            cnt+=1
        K-=i
    if cnt > M or mid < max(money):
        start = mid + 1
    else: 
        end = mid - 1
        ans = mid
    
print(ans)