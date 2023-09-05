# https://www.acmicpc.net/problem/1748

N = input()
compare = len(N) - 1
answer = 0

for i in range(compare):
    answer += 9 * (10**i) * (i+1)
    i+=1
answer += (int(N) - (10 ** compare) + 1) * (compare + 1)
print(answer)