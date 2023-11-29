import sys
import string
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

refuse = 0
new_l = []
for i in range(n):
    if l[i] in new_l:
        refuse += 1
        continue
    new_l.append(l[i])

print(refuse)
