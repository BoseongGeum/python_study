import sys
input = sys.stdin.readline

d = {}
s = 0
for _ in range(10):
    n = int(input())
    if n in d.keys():
        d[n] += 1
    else:
        d[n] = 1
    s += n

print(s//10)

mode = d[list(d.keys())[0]]
m = list(d.keys())[0]

for n in d.keys():
    if mode < d[n]:
        mode = d[n]
        m = n
        
    
print(m)
