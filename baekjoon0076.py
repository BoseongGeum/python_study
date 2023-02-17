import sys
import collections

n = int(input())
l = []
for x in range(n):
    l.append(int(sys.stdin.readline().rstrip()))
l.sort()
print(round(sum(l)/len(l)))
print(l[n//2])
c = collections.Counter(l).most_common()
try:
    if c[0][1] == c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])
except:
    print(l[0])
print(l[n-1] - l[0])
