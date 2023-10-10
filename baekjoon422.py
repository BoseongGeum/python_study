import sys
input = sys.stdin.readline

l = []
l1 = []

for _ in range(10):
    l.append(int(input()))

for _ in range(10):
    l1.append(int(input()))

print(sorted(l)[7]+sorted(l)[8]+sorted(l)[9],
      sorted(l1)[7]+sorted(l1)[8]+sorted(l1)[9])
