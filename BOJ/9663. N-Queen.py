# https://www.acmicpc.net/problem/9663

import sys
input = sys.stdin.readline

n = int(input())

def check(row):
    for x in range(row):
        if(queen[x] == queen[row] or 
           abs(queen[x]-queen[row])==abs(x-row)):
            return False
    return True

cnt = 0
queen = [0] * n 
def dfs(row):
    global cnt
    if row == n:
        cnt += 1
    else:
        for col in range(n):
            queen[row] = col
            if check(row):
                dfs(row+1)

dfs(0)
print(cnt)


#######################
# Python3로는 시간초과   #
# 	PyPy3로 통과       #
######################