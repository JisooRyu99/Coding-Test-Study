# (Silver 4) 11399. ATM
T = int(input())
s = 0
bank = list(map(int, input().split()))
bank.sort()

for i in range(T+1):
    s+=sum(bank[:i])
print(s)