import sys
input = sys.stdin.readline

n = int(input())
l = []

for _ in range(n):
    a, b = input().split()
    l.append([b, a])
    
l.sort()
print(l[0][1])
