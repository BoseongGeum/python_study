import sys
input = sys.stdin.readline

l = [0, 0, 0, 0]

for i in range(4):
    l[i] = int(input())
    
t = sum(l)
m = t // 60
s = t % 60

print(m)
print(s)
