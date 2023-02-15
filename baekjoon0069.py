import math

l = []
for x in range(9):
    l += list(map(int, input().split()))
print(max(l))
b = l.index(max(l))+1
a = b%9
if a == 0:
    a = 9
print(math.ceil(b/9), a)
