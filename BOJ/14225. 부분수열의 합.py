# https://www.acmicpc.net/problem/14225

import sys

input = sys.stdin.readline

n = int(input())
S = list(map(int, input().split()))

S.sort()
answer = 0
for i in S:
    if answer + 1 <i: break
    answer+=i
print(answer+1)
