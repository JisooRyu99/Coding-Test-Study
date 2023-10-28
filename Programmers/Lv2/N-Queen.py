# https://school.programmers.co.kr/learn/courses/30/lessons/12952

def dfs(queen,n,row):
    count=0
    if n==row:
        return 1
    for col in range(n):
        queen[row] = col
        for x in range(row):
            if abs(queen[row]-queen[x])==(row-x) or queen[x]==queen[row]:
                break
        else:
            count+=dfs(queen,n,row+1)
    return count
def solution(n):
    answer = [-1]*n
    return dfs(answer,n,0)