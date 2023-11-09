import sys
import heapq 

sys.setrecursionlimit(10**9)        
input = sys.stdin.readline

T = int(input())
stack = []

for _ in range(T):
    num = list(map(int, input().split()))
    
    if num[0] == 1: stack.append(num[1])
    elif num[0] == 2:
        if stack: print(stack.pop())
        else: print(-1)
    elif num[0] == 3: print(len(stack))
    elif num[0] == 4:
        if stack: print(0)
        else: print(1)
    else:
        if stack: print(stack[-1])
        else: print(-1)