# https://www.acmicpc.net/problem/15903

import heapq

N, M = map(int, input().split())
card = list(map(int, input().split()))
heapq.heapify(card)

while True:
    if M <= 0: break
    num1 = heapq.heappop(card)
    num2 = heapq.heappop(card)

    heapq.heappush(card, num1+num2)
    heapq.heappush(card, num1+num2)
    M-=1
print(sum(card))