from heapq import heappush, heappop

N = int(input())
decks = []
for _ in range(N):
    heappush(decks, int(input()))

total = 0
while len(decks) > 1:
    comp = heappop(decks) + heappop(decks)
    total += comp
    heappush(decks, comp)

print(total)