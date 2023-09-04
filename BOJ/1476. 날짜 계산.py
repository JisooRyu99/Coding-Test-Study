# https://www.acmicpc.net/problem/1476

E, S, M = map(int, input().split())
date = [0,0,0]
cnt=0
while True:
    if date[0] == E and date[1] == S and date[2] == M :
        break
    if date[0] > 14: date[0] = 0
    if date[1] > 27: date[1] = 0
    if date[2] > 18: date[2] = 0
    
    date[0] += 1
    date[1] += 1
    date[2] += 1
    cnt+=1
print(cnt)