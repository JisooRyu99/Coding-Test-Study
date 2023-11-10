# https://www.acmicpc.net/problem/10867

x = int(input())
result= list(map(int, input().split()))
for i in sorted(set(result)):
    print(i, end=' ')