l = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))


A.sort()
B.sort(reverse=1)
print(A)
print(B)
sum=0
for i in range(l):
    sum += A[i]*B[i]
print(sum)
