import sys

l1 = []
l2 = []
t1 = True
t2 = True

while t1:
    a, b = map(int, sys.stdin.readline().rstrip().split())
    l1.append(a)
    l2.append(b)
    if a == 0 and b == 0:
       t1 = False
       
while t2:
    print(l1[0] + l2[0])
    del l1[0]
    del l2[0]
    if l1[0] == 0 and l2[0] == 0:
       t2 = False 
