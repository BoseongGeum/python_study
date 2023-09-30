import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = 0
    l = list(map(int, input().split()))
    m = max(l)
    for i in l:
        if i % 2 == 0:
            s += i
            if m > i:
                m = i
    print(s, m)
