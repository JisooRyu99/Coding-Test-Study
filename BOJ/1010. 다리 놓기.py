from math import factorial
T = int(input())
for i in range(T):
    m, n = map(int, input().split())
    result = factorial(n) // (factorial(n-m) * factorial(m))

    print(result)
