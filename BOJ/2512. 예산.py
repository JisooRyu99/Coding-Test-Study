# https://www.acmicpc.net/problem/2512

N = int(input())
budge = list(map(int, input().split()))
total_max = int(input())

start, end = 0, max(budge)
while start <= end:
    mid = (start+end) // 2
    total = 0
    for i in budge:
        if i > mid:
            total += mid
        else:
            total += i
    if total <= total_max:
        start = mid+1
    else:
        end = mid - 1
print(end)