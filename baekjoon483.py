import sys
input = sys.stdin.readline

t1 = list(map(int, input().split()))
t2 = list(map(int, input().split()))
t3 = list(map(int, input().split()))

l = [t1, t2, t3]
for t in l:
    if t[2] > t[5]:
        if t[4] == 0:
            t[3] -= 1
            t[4] += 60
        t[4] -= 1
        t[5] += 60
    s = t[5] - t[2]
    
    if t[1] > t[4]:
        t[3] -= 1
        t[4] += 60
    m = t[4] - t[1]
    
    h = t[3] - t[0]

    print(h, m, s)
