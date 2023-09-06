# https://www.acmicpc.net/problem/15657

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
result= []
def dfs(start):
    if len(result)==m:
        print(" ".join(map(str,result)))
        return
    for i in range(start,len(arr)):
        result.append(arr[i])
        dfs(i)
        result.pop()


dfs(0)