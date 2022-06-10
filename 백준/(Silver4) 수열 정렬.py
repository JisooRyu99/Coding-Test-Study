import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

result = []
sorted_A = sorted(A)

for i in A:
    result.append(sorted_A.index(i))    # index 탐색
    sorted_A[sorted_A.index(i)] = -1    # 탐색한 index는 다시 찾지 못하게 만듦
  
print(*result)
