import sys
import collections

n = int(input())
c = collections.Counter(sys.stdin.readline().rstrip().split())
m = int(input())
l = sys.stdin.readline().rstrip().split()
d = {key : value for key, value in c.items()}

l2 = [d[x] if x in d else 0
      for x in l]
print(*l2)
