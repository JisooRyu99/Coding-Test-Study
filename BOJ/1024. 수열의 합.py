# https://www.acmicpc.net/problem/1024

N, L = map(int, input().split())
answer = []

for i in range(L, 101):
    idx = N - (i *(i+1) // 2)
    if idx % i==0:
        x = idx // i
        if x+1 >=0:
            print(*(i for i in range(x+1, x + i+1)))
            break
else: print(-1)