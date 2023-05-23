import sys
input = sys.stdin.readline

s = 0
curs = []
for _ in range(4):
    a, b = map(int, input().split())
    s += b - a
    curs.append(s)
    
print(max(curs))
