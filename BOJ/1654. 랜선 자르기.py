N, K = map(int, input().split())
lan = [int(input()) for _ in range(N)]
start, end = 1, max(lan)

while start <= end:
    mid = (start+end)//2
    total = 0
    
    for l in lan:
        total+= l//mid
    if total>=K: start = mid+1
    else: end = mid-1

print(end)