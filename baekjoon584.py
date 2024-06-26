import sys
input = sys.stdin.readline
from collections import defaultdict

cards = defaultdict(list)

for _ in range(5):
    a, b = input().split()
    cards[a].append(int(b))

sf = [k for k, v in cards.items() if len(v) == 5]
if sf != [] and max(cards[sf[0]]) - min(cards[sf[0]]) == 4:
    print(900 + max(cards[sf[0]]))
