import sys
input = sys.stdin.readline

n, k = map(int, input().split())
l = list(map(int, list(input().rstrip()))) + [-1]

start = 0
maxv = 0
while k > 0:
    for i in range(start, start+k+1):
        if l[i] == -1:
            maxi = len(l) - 1
            break
        if l[i] > maxv:
            maxv = l[i]
            maxi = i

    for _ in range(start, maxi):
        del l[start]
    k -= maxi - start
    start += 1
    maxv = 0
    maxi = 0

del l[-1]
for x in l:
    print(x, end='')
