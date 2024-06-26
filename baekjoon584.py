import sys
input = sys.stdin.readline
from collections import defaultdict

cardColor = defaultdict(list)
cardNum = defaultdict(list)

for _ in range(5):
    a, b = input().split()
    cardColor[a].append(int(b))
    cardNum[int(b)].append(a)

fl = [k for k, v in cardColor.items() if len(v) == 5]
fc = [k for k, v in cardNum.items() if len(v) == 4]
tr = [k for k, v in cardNum.items() if len(v) == 3]
pa = [k for k, v in cardNum.items() if len(v) == 2]
st = [k for k, v in cardNum.items() if len(v) == 1]

if fl and max(cardColor[fl[0]]) - min(cardColor[fl[0]]) == 4:
    print(900 + max(cardColor[fl[0]]))

elif fc:
    print(800 + fc[0])

elif tr and pa:
    print(700 + tr[0]*10 + pa[0])

elif fl:
    print(600 + max(cardColor[fl[0]]))

elif len(st) == 5 and max(st) - min(st) == 4:
    print(500 + max(st))

elif tr:
    print(400 + tr[0])

elif len(pa) == 2:
    print(300 + max(pa)*10 + min(pa))

elif pa:
    print(200 + pa[0])

else:
    print(100 + max(cardNum.keys()))
