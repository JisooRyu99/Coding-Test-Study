# https://www.acmicpc.net/problem/1715

import heapq

N = int(input())
card = [int(input()) for _ in range(N)]

heapq.heapify(card)
S = 0

while len(card) > 1:
    card1 = heapq.heappop(card)
    card2 = heapq.heappop(card)
    S+=(card1+card2)
    heapq.heappush(card, card1+card2) 
print(S)