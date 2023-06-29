import sys
input = sys.stdin.readline

n = int(input())
v = list(map(int, input().split())) + [0, 0]

s = 0
for i in range(n):
    if v[i+1] > v[i+2]:
        g = min(v[i], v[i+1] - v[i+2])
        s += g * 5
        v[i] -= g
        v[i+1] -= g

        g = min(v[i], v[i+1])
        s += g * 7
        v[i] -= g
        v[i+1] -= g
        v[i+2] -= g

    else:
        g = min(v[i], v[i+1])
        s += g * 7
        v[i] -= g
        v[i+1] -= g
        v[i+2] -= g

    s += v[i] * 3

print(s)
