import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

h = []
for i in range(n):
    h.append([b[i], a[i]])

s = 0
minr = 0
for i in range(n):
    d, r = heappop(h)
    if minr > r:
        c = (minr - r) // 30 + 1
        r += 30 * c
        s += c
        heappush(h, [d, r])
        
    else:
        minr = r
        
for i in range(n):
    d, r = heappop(h)
    if d > r:
        c = (d - r) // 30 + 1
        r += 30 * c
        s += c
    heappush(h, [d, r])


    print(r)
        

print(s)
