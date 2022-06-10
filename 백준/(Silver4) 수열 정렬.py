import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

result = []
sorted_A = sorted(A)

for i in A:
    result.append(sorted_A.index(i))
    sorted_A[sorted_A.index(i)] = -1
print(*result)
