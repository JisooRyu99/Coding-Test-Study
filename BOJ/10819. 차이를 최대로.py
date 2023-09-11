# https://www.acmicpc.net/problem/10819

n=int(input())
arr = list(map(int,input().split()))
answer = 0

from itertools import permutations

data = list(permutations(arr,n))

for i in range(len(data)):
    tmp = 0
    for j in range(1,len(data[i])):
        tmp+=abs(data[i][j-1]-data[i][j])
    answer = max(answer,tmp)
print(answer)