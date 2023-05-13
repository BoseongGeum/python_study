import sys
input = sys.stdin.readline

allstr = input().rstrip()
searchstr = input().rstrip()

al = len(allstr)
sl = len(searchstr)
i = 0
c = 0

while al >= i + sl:
    if allstr[i:i+sl] == searchstr:
        i += sl
        c += 1
    else:
        i += 1
        
print(c)
