import sys
input = sys.stdin.readline

l = []
for _ in range(9):
    t = int(input())
    l.append(t)

r = sum(l) - 100
a = r // 2
b = r - a
if a == b:
    a -= 1
    b += 1
while a != 1:
    if a in l and b in l:
        break
    a -= 1
    b += 1
l.remove(a)
l.remove(b)

for i in l:
    print(i)
