import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
lenlist = []
curmax = 0

for x in range(n):
    if curmax < l[x]:
        curmax = l[x]
        lenlist.append(l[x])
        curlen += 1
        maxlen += 1
    else:
        curlen = 0
        
    if curlen > maxlen:
        maxlen = curlen

20 50 10 20 30 40
