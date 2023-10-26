# https://www.acmicpc.net/problem/2805

N, M = map(int, input().split())
log = list(map(int, input().split()))
start, end = 1, max(log)

while start<=end:
    mid = (start + end)//2
    total = 0
    for i in log:
        if i>= mid:
            total += (i-mid)
    
    if total>=M:
        start = mid + 1
    else:
        end = mid - 1
print(end)