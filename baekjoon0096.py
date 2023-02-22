import sys

n, m = map(int, input().split())
l1 = []
c = 0
for x in range(n):
    l1.append(sys.stdin.readline().rstrip())
for x in range(m):   
    s = sys.stdin.readline().rstrip()
    try:
        if type(int(s)) == int:
            print(l1[int(s)-1])
    except:
            print(l1.index(s) + 1)
